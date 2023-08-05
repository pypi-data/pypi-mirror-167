"""Exceptions for mcping"""


class MCPingException(Exception):
    """Base exception for all other mcping exceptions"""


class InvalidResponseError(MCPingException):
    """For invalid responses from server, eg. malformed response packet or invalid JSON in status"""


class ServerTimeoutError(MCPingException):
    """For if the server fails to respond in time"""
