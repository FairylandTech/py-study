# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-18 11:39:05 UTC+08:00
"""

import functools
from functools import wraps
from typing import Callable, TypeVar, Generic, Any
from typing import Type

_T = TypeVar("_T", bound=Callable[..., Any])


class BaseDecorator(Generic[_T]):
    """
    Base decorator class

    :param func: decorated function
    :type func: Callable[..., Any]
    :return: decorated function
    :rtype: Callable[..., Any]

    Usage:
        >>> @BaseDecorator
        >>> def my_decorator(func):
        >>>     @wraps(func)
        >>>     def wrapper(*args, **kwargs):
        >>>         return func(*args, **kwargs)
        >>>     return wrapper
        >>> @my_decorator
        >>> def my_func():
        >>>     pass
        >>> my_func()
        >>> # output: None
    """

    def __init__(self, func: Type):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return self.__class__(self.func.__get__(instance, owner))


class BaseParamsDecorator(Generic[_T]):
    """
    Base decorator class with parameters

    :param func: decorated function
    :type func: Callable[..., Any]
    :return: decorated function
    :rtype: Callable[..., Any]

    Usage:
        >>> @BaseParamsDecorator(1, 2, 3)
        >>> def my_decorator(func):
        >>>     @wraps(func)
        >>>     def wrapper(*args, **kwargs):
        >>>         return func(*args, **kwargs)
        >>>     return wrapper
        >>> @my_decorator
        >>> def my_func():
        >>>     pass
        >>> my_func()
        >>> # output: None
    """

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def __call__(self, *args, **kwargs):
        if args and len(args) == 1 and callable(args.__getitem__(0)):
            self.func: Type = args.__getitem__(0)

        @wraps(self.func)
        def wrapper(*args, **kwargs):
            return self.func(*args, **kwargs)

        return wrapper

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return self.__class__(self.func.__get__(instance, owner))
