import pytest
from pytest_mock import MockerFixture

import myqiwi


wallet = myqiwi.AsyncWallet("test")


async def _get_empty_response_object(status=200, json_=None):
    async def json(*args, **kwargs):
        return json_ or {}

    async def text(*args, **kwargs):
        return ""

    return type("Response", (), {"status": status, "json": json, "text": text})()


async def _mock_get_profile(mocker: MockerFixture):
    mocker.patch(
        "aiohttp.ClientSession.request",
        return_value=_get_empty_response_object(json_={"contractInfo": {"contractId": "123456789"}})
    )
    await wallet.profile


@pytest.mark.asyncio
async def test_get_balance(mocker: MockerFixture):
    await _mock_get_profile(mocker)

    return_value = {"accounts": [{"currency": 643, "balance": {"amount": "1.00"}}]}

    mocker.patch("myqiwi.request.make_request", return_value=return_value)
    assert await wallet.balance() == 1

    try:
        await wallet.balance(currency=555)
        assert False  # pragma: no cover
    except myqiwi.exceptions.CurrencyInvalid:
        assert True
