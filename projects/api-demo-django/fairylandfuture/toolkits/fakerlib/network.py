# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-10-15 17:13:42 UTC+08:00
"""

from faker import Faker

from fairylandfuture.core.superclass.toolkits.fakerlib import BaseFaker


class FakeNetworkToolkits(BaseFaker):

    @classmethod
    def __route(cls, locale=None):
        if locale and locale.upper() in ("ZH_CN", "CN"):
            cls.faker = cls.faker_zh
            return cls.faker
        else:
            cls.faker = cls.faker_en
            return cls.faker

    @classmethod
    def generate_ipv4_address(cls):
        return cls.__route().ipv4()
