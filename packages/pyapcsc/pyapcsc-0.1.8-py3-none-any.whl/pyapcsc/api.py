import aiohttp

from .login_helper import LoginHelper
from .exceptions import UnauthorizedException, ApiError


class ApcSmartConnectApi:
    """ API wrapper for access the APC Smart Connect API. """

    def __init__(self, session: aiohttp.ClientSession):
        self._headers = {}
        self._session = session
        self._cookies = {}

    async def login(self, username, password) -> None:
        self._cookies = {}
        helper = LoginHelper(self._session, self._cookies)

        await helper.login(username, password)

    async def gateways(self) -> list[str]:
        return await self._get("gateways")

    async def gateway(self, gateway_id: str) -> dict:
        return await self._get(f"gateways/{gateway_id}")

    async def gateway_details(self, gateway_id: str) -> dict:
        return await self._get(f"gateways/{gateway_id}?collection=input,output,battery,network,main_outlet,switched_outlets")

    async def _get(self, path):
        response = await self._session.get(f"https://smartconnect.apc.com/api/v1/{path}", cookies=self._cookies)

        try:
            response.raise_for_status()
        except aiohttp.ClientResponseError as ex:
            if ex.status == 403:
                raise UnauthorizedException from ex

            raise ApiError from ex
        return await response.json()
