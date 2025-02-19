# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-10-18 14:15:39 UTC+08:00
"""

from faker import Faker


class BaseFaker:
    faker_zh = Faker("zh_CN")
    faker_en = Faker("en_US")
