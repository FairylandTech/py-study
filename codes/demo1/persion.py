# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-12 22:07:59 UTC+08:00
"""

import abc
from datetime import datetime


class Person:

    def __init__(self, name, birthday, gender, level):
        self.__name = name
        self.__birthday = birthday
        self.__gender = gender
        self.__level = level

    @property
    def birthday(self):
        return self.__birthday

    @property
    def age(self):
        return datetime.now().year - int(self.__birthday.split("-")[0])

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    @abc.abstractmethod
    def show(self): ...
