# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-17 17:50:47 UTC+08:00
"""

from fairylandfuture.core.superclass.exceptions.exception import BaseProgramException


class ElasticSearchExecutionException(BaseProgramException):

    def __init__(self, message):
        super().__init__(message)
