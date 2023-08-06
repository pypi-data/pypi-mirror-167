"""Helper classes for logging into the API. """

import aiohttp
import re

INIT_AUTH_URL = "https://smartconnect.apc.com/auth/login"
AUTH_BASE = "https://secureidentity.schneider-electric.com"
LOGIN_URL = f"{AUTH_BASE}/identity/UserLogin"
USERNAME_FIELD_ID = "j_id0:j_id65:j_id79"
PASSWORD_FIELD_ID = "j_id0:j_id65:j_id83"


class LoginHelper:
    """ API wrapper for access the APC Smart Connect API. """

    def __init__(self, session: aiohttp.ClientSession, cookies: dict):
        self._session = session
        self._cookies = cookies

    async def login(self, username: str, password: str) -> dict:
        text = await self._get(INIT_AUTH_URL)
        self._parse_cookies(text)

        text = await self._get(AUTH_BASE + get_window_location(text))

        text = await self._send_login(text, username, USERNAME_FIELD_ID)
        text = await self._send_login(text, password, PASSWORD_FIELD_ID)

        # Need to follow the redirect chain to finish the auth
        # This might be a bit fragile given the assumptions around the flows
        calls = [
            get_meta_url,
            get_window_location,
            get_window_location,
            get_window_location
        ]
        for call in calls:
            text = await self._get(call(text))

    def _parse_cookies(self, page: str) -> None:
        matches = re.finditer('document.cookie = "(.*?)=(.*?);', page)
        for match in matches:
            self._cookies[match.group(1)] = match.group(2)

    async def _get(self, url: str) -> str:
        response = await self._session.get(url, cookies=self._cookies)
        response.raise_for_status()
        return await response.text()

    async def _send_login(self, page: str, username: str, step_id: str) -> str:
        data = {
            "AJAXREQUEST": "_viewRoot",
            "j_id0:j_id65": "j_id0:j_id65",
            step_id: step_id,
            "usrname": username
        }

        matches = re.finditer('name="(com.salesforce.visualforce.ViewState(?:.*?))" value="(.+?)"', page)
        for match in matches:
            data[match.group(1)] = match.group(2)

        response = await self._session.post(LOGIN_URL, data=data, cookies=self._cookies)
        response.raise_for_status()
        return await response.text()


def get_window_location(page: str) -> str:
    matches = re.search("window.location(?:.href)? =(?:\\'| \")(.*?)(?:\\'|\");", page)
    if (not matches):
        matches = re.search(r"window.location.replace\(\"(.*?)\"\);", page)
        return AUTH_BASE + matches.group(1)
    return matches.group(1)


def get_meta_url(page: str) -> str:
    matches = re.search('<meta name="Location" content="(.+?)"', page)
    return matches.group(1)
