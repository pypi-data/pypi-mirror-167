# pyapcsc
Python Client for APC Smart connect

# Usage
The library offers two class for interacting with the API.

## API
Provides direct access to the API. Return types are the deserialized json objects.
```
async with aiohttp.ClientSession() as websession:
    websession._default_headers = MappingProxyType({})  # type: ignore
    client = pyapcsc.ApcSmartConnectApi(websession)
    await client.login("username", "password")
    gateways = await client.gateways()
    await websession.close()
```

## Client
The client class offers a typed abstraction over the API. Also the client will handle reauthenticating when the existing cookie expires.
```
async with aiohttp.ClientSession() as websession:
    websession._default_headers = MappingProxyType({})  # type: ignore
    client = pyapcsc.ApcSmartConnectClient(websession)
    await client.login("username", "password")
    gateways = await client.gateways()
    await websession.close()
```

