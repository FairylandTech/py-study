# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-12 22:06:50 UTC+08:00
"""
from datetime import datetime
from .persion import Person


class Admin(Person):

    def show(self):
        print(f"管理员: Name: {self.name}, Birthday: {self.birthday}, Age: {self.age}, Gender: {self.gender}, Level: {self.level}")
