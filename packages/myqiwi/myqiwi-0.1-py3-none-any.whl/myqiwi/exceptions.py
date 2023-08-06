class BaseQiwiException(Exception):
    status_code = None


class BaseExtendQiwiException(BaseQiwiException):
    def __init__(self, data: dict, text=None):
        super().__init__(text or self.__class__.__name__)
        self.data = data
        self.code = self.data.get("code", None)
        self.message = self.data.get("message", None)


class StatusError(BaseExtendQiwiException):
    pass


class Status404Error(StatusError):
    status_code = 404


class ArgumentError(BaseExtendQiwiException):
    pass


class InvalidToken(BaseExtendQiwiException):
    pass


class NotHaveEnoughPermissions(BaseExtendQiwiException):
    pass


class NoTransaction(Status404Error):
    pass


class NotFoundActiveWebhook(Status404Error):
    pass


class NeedPhone(BaseQiwiException):
    pass


class CurrencyInvalid(BaseQiwiException):
    pass
