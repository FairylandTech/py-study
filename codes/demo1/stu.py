# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-12 21:54:27 UTC+08:00
"""
from datetime import datetime

from .persion import Person


class Student(Person):

    def show(self):
        print(f"学生: Name: {self.name}, Birthday: {self.birthday}, Age: {self.age}, Gender: {self.gender}, Level: {self.level}")
