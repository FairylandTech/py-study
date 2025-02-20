# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-10 18:29:47 UTC+08:00
"""

from fairylandfuture.core.superclass.exceptions.exception import BaseProgramException


class ParamsInvalidException(BaseProgramException):

    def __init__(self, message: str = "Parameter error."):
        super().__init__(message)


class ParamsTypeException(BaseProgramException):

    def __init__(self, message: str = "Parameter type error."):
        super().__init__(message)


class ParamsValueException(BaseProgramException):

    def __init__(self, message: str = "Parameter value error."):
        super().__init__(message)


class ValidationError(BaseProgramException):
    def __init__(self, message: str = "Validation error."):
        self.message = message
        super().__init__(self.message)
