# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-18 00:56:51 UTC+08:00
"""

from fairylandfuture.core.superclass.enums.enumerate import BaseEnum


class LogLevelEnum(BaseEnum):
    """
    Log level Enum.
    """

    trace = "TRACE"
    debug = "DEBUG"
    info = "INFO"
    success = "SUCCESS"
    warning = "WARNING"
    error = "ERROR"
    critical = "CRITICAL"

    default = info
