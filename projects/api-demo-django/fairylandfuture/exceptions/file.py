# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-10 18:32:09 UTC+08:00
"""

from fairylandfuture.core.superclass.exceptions.exception import BaseProgramException


class FileReadException(BaseProgramException):

    def __init__(self, message: str = "File read error."):
        super().__init__(message=message)
