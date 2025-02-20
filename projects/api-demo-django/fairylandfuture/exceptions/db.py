# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-10 18:31:36 UTC+08:00
"""

from fairylandfuture.core.superclass.exceptions.exception import BaseProgramException


class SQLExecutionException(BaseProgramException):

    def __init__(self, message: str = "SQL execution error."):
        super().__init__(message=message)


class SQLSyntaxException(BaseProgramException):

    def __init__(self, message: str = "SQL syntax error."):
        super().__init__(message=message)
