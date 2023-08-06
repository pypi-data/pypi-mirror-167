import typing
import fastapi
import asyncio

from myqiwi.utils import is_qiwi_api


class SimpleRequestHandler:
    def register(self, app: typing.Union[fastapi.FastAPI, fastapi.APIRouter], path, route_name="qiwi_webhook"):
        app.add_api_route(path, self.handle, methods=["POST"], name=route_name, include_in_schema=False)
        return self

    async def handle(self, request: fastapi.Request):
        if is_qiwi_api(self.extract_ip_from_request(request)):
            asyncio.create_task(self._handle_request((await request.json())["payment"]))

        return fastapi.responses.Response(status_code=200)

    async def _handle_request(self, transaction: dict):
        raise NotImplementedError
        # comment = transaction["comment"]
        # amount = transaction["sum"]["amount"]
        # currency = int(transaction["currency"])

    @classmethod
    def extract_ip_from_request(cls, request: fastapi.Request):
        return request.client.host
