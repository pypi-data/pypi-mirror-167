import time

from . import request
from . import exceptions


class AsyncWallet:
    __PAYMENT_FORM_URL = "https://qiwi.com/payment/form/"

    def __init__(self, token: str):
        self.__token = token

    @property
    async def number(self):
        return (await self.profile)["contractInfo"]["contractId"]

    @property
    async def username(self):
        return (await self.profile)["contractInfo"]["nickname"]["nickname"]

    async def balance(self, currency=643):
        path = "funding-sources/v2/persons/{}/accounts".format(await self.number)
        response = await self.get(path)

        for i in response["accounts"]:
            if int(i["currency"]) == currency:
                balance = float(i["balance"]["amount"])
                break
        else:
            raise exceptions.CurrencyInvalid

        return balance

    @property
    async def profile(self) -> dict:
        if not hasattr(self, "_profile"):
            setattr(self, "_profile", await self.get_profile())
        return getattr(self, "_profile")

    async def get_profile(self) -> dict:
        return await self.get("/person-profile/v1/profile/current")

    async def history(self, rows=20, currency=None, operation=None):
        """
        История платежей
        Warning
        -------
        Максимальная интенсивность запросов истории платежей -
        не более 100 запросов в минуту
         для одного и того же номера кошелька.
        При превышении доступ к API блокируется на 5 минут.

        Parameters
        ----------
        rows : Optional[int]
            Число платежей в ответе, для разбивки отчета на части.
            От 1 до 50, по умолчанию 20.
        currency : optional[int]
            ID валюты в ``number-3 ISO-4217``, с которорой будут показываться
            переводы.
            По умолчанию None, значит будут все переводы
            Например, 643 для российского рубля.
        operation : Optional[str]
            Тип операций в отчете, для отбора.
            Варианты: IN, OUT, QIWI_CARD.
            По умолчанию - ALL.
        
        Returns
        -------
        dict
        """
        _history = await self.get(
            "payment-history/v2/persons/{}/payments".format(await self.number), params={"rows": rows}
        )
    
        history = []

        for transaction in _history["data"]:
            if currency:
                if transaction["total"]["currency"] != currency:
                    continue

            if operation:
                if transaction["type"] != operation:
                    continue

            transaction = {
                "account": transaction["account"],
                "comment": transaction["comment"],
                "commission": transaction["commission"],
                "date": transaction["date"],
                "status": transaction["statusText"],
                "sum": transaction["total"],
                "trmTxnId": transaction["trmTxnId"],
                "txnId": transaction["txnId"],
                "type": transaction["type"],
            }
            history.append(transaction)

        return history

    @classmethod
    def generate_pay_form(
            cls, phone=None, username=None, _sum=None, comment="", currency=643
    ):
        if phone:
            form = 99
        else:
            form = 99999
            phone = username

        url = cls.__PAYMENT_FORM_URL + str(form) + "?"
        url += "extra%5B%27account%27%5D={}".format(phone)
        url += "&amountInteger={}&amountFraction=0&".format(_sum)
        url += "extra%5B%27comment%27%5D={}".format(comment)
        url += "&currency={}&blocked[0]=account".format(currency)

        if _sum:
            url += "&blocked[1]=sum"
        if comment:
            url += "&blocked[2]=comment"

        return url

    async def send_money(self, number, _sum, comment=None, currency=643):
        """
        Перевод средств на другой киви кошелёк.
        Parameters
        ----------
        number : str
            Номер, куда нужно перевести.
        _sum : currency
            Сумма перевода. Обязательно в рублях
        comment : Optional[str]
            Комментарий к платежу
        currency : optional[int]
            ID валюты в ``number-3 ISO-4217``, с которорой будут показываться
            переводы.
            По умолчанию None, значит будут все переводы
            Например, 643 для российского рубля.

        Returns
        -------
        dict
        :param comment:
        :param _sum:
        :param number:
        :param currency:
        """
        _json = {
            "id": str(int(time.time() * 1000)),
            "sum": {"amount": str(_sum), "currency": str(currency)},
            "paymentMethod": {"type": "Account", "accountId": "643"},
            "comment": comment,
            "fields": {"account": str(number)}
        }

        path = "sinap/api/v2/terms/99/payments"
        _history = await self.post(path, json=_json)

    async def search_payment(self, comment, need_sum=0, currency=643):
        payments = await self.history(rows=50, currency=currency, operation="IN")
        response = {"status": False}

        _sum = 0
        amount_transactions = 0

        for payment in payments:
            if comment == payment["comment"]:
                amount_transactions += 1
                _sum += payment["sum"]["amount"]

        if (0 == need_sum and 0 < _sum) or (0 < need_sum <= _sum):
            response["sum"] = _sum
            response["status"] = True
            response["amount_transactions"] = amount_transactions

        return response

    async def check_restriction_out_payment(self):
        await self.need_number()

        path = "person-profile/v1/persons/{}/status/restrictions".format(self.number)
        response = await self.post(path)

        condition = 0 < len(response)
        """[{'restrictionCode': 'OUTGOING_PAYMENTS', 'restrictionDescription': 'Исходящие платежи заблокированы'}]"""
        if condition and "restrictionCode" in response[0] and response[0]["restrictionCode"] == "OUTGOING_PAYMENTS":
            response = True

        return response

    async def payment_notifier(self, param, txn_type=0):
        path = "/payment-notifier/v1/hooks"
        params = {
            "hookType": 1,
            "param": param,
            "txnType": txn_type
        }
        return await self.request("put", path, params=params)

    async def delete_payment_notifier(self, hook_id):
        path = "/payment-notifier/v1/hooks/{}".format(hook_id)
        return await self.request("delete", path)

    async def get_payment_notifier(self):
        path = "/payment-notifier/v1/hooks/active"
        try:
            return await self.get(path)
        except exceptions.Status404Error:
            raise exceptions.NotFoundActiveWebhook({})

    async def test_payment_notifier(self):
        return await self.get("/payment-notifier/v1/hooks/test")

    async def need_number(self):
        if getattr(self, "number", None) is None:
            profile = await self.profile()

            self.__number = profile["contractInfo"]["contractId"]
            self.__username = profile["contractInfo"]["nickname"]["nickname"]

    async def request(self, method: str, path: str, **kwargs):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.__token),
        }
        return await request.make_request(method, path, headers=headers, **kwargs)

    async def get(self, path, **kwargs):
        return await self.request("get", path, **kwargs)

    async def post(self, path, **kwargs):
        return await self.request("get", path, **kwargs)
