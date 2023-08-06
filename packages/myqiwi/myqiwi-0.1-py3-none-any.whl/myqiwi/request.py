import aiohttp

from myqiwi import exceptions

API_URl = "https://edge.qiwi.com/"


async def check_result(response: aiohttp.ClientResponse):
    data = await response.json(content_type=None) or {"code": "", "message": ""}
    error_text = await response.text()

    if 400 == response.status:
        raise exceptions.ArgumentError(data, text=error_text)
    if 401 == response.status:
        raise exceptions.InvalidToken(data, text="Invalid token")
    if 403 == response.status:
        raise exceptions.NotHaveEnoughPermissions(data, text=error_text)
    if exceptions.Status404Error.status_code == response.status:
        raise exceptions.Status404Error(data, text=error_text)


async def make_request(method: str, path: str, **kwargs) -> dict:
    url = "{}{}".format(API_URl, path)

    async with aiohttp.ClientSession() as session:
        response = await session.request(method, url, **kwargs)

    await check_result(response)

    return await response.json()
