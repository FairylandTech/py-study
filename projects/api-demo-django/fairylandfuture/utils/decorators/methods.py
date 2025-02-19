# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-25 13:43:08 UTC+08:00
"""


from typing import Callable, Any, TypeVar

_T = TypeVar("_T", bound=Callable[..., Any])


class TryCatchMethodDecorator:
    def __init__(self, func: _T):
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        except Exception as err:
            raise err
