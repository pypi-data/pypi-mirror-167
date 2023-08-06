"""Test entry point"""

import aiohttp
import pyapcsc
import argparse
import asyncio
import logging
from types import MappingProxyType

LOGGER = logging.getLogger(__name__)


async def main():
    """Main function."""
    LOGGER.info("Starting")

    async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar(unsafe=True)) as websession:
        websession._default_headers = MappingProxyType({})  # type: ignore
        client = pyapcsc.ApcSmartConnectClient(websession)
        await client.login("", "")
        gateways = await client.gateways()
        gateway = await client.gateway(gateways[0])
        LOGGER.info(gateway.name)
        gateway_details = await client.gateway_details(gateways[0])
        LOGGER.info(gateway_details.battery.runtime_remaining)

        await websession.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", type=bool, default=False)
    args = parser.parse_args()

    LOG_LEVEL = logging.INFO
    if args.debug:
        LOG_LEVEL = logging.DEBUG
    logging.basicConfig(format="%(message)s", level=LOG_LEVEL)

    try:
        asyncio.run(
            main()
        )
    except KeyboardInterrupt:
        pass
