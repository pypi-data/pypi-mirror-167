""" Helper client for working with SmartConnect. """

import aiohttp
from .api import ApcSmartConnectApi
from .exceptions import UnauthorizedException
from .dtos import Gateway, GatewayDetails


class ApcSmartConnectClient:
    """ SmartConnect client. """

    _username = None
    _password = None
    _logged_in = False

    def __init__(self, session: aiohttp.ClientSession):
        self._api = ApcSmartConnectApi(session)

    async def login(self, username: str, password: str) -> None:
        await self._api.login(username, password)
        self._username = username
        self._password = password
        self._logged_in = True

    async def gateways(self) -> list[str]:
        return await self._perform_api_request(self._api.gateways)

    async def gateway(self, device_id: str) -> Gateway:
        json = await self._perform_api_request(lambda: self._api.gateway(device_id))
        return Gateway(json)

    async def gateway_details(self, device_id: str) -> GatewayDetails:
        json = await self._perform_api_request(lambda: self._api.gateway_details(device_id))
        return GatewayDetails(json)

    async def _perform_api_request(self, func) -> any:
        if (not self._logged_in):
            raise UnauthorizedException("Not logged in")

        try:
            return await func()
        except UnauthorizedException:
            self._logged_in = False
            await self._api.login(self._username, self._password)
            self._logged_in = True
            return await func()
