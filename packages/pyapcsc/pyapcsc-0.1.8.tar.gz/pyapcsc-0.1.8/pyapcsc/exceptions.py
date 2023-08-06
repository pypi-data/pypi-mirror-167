""" Library exception defs """


class ApcSmartConnectException(Exception):
    """Base Exception"""


class ApiError(ApcSmartConnectException):
    """Base API Exception"""


class UnauthorizedException(ApiError):
    """Indicate the client is not authorized to communicate with the server."""
