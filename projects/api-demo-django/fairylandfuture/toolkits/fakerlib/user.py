# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-10-15 16:05:32 UTC+08:00
"""

from datetime import datetime
from faker import Faker
from pypinyin import pinyin, Style

from fairylandfuture.core.superclass.toolkits.fakerlib import BaseFaker


class FakeUserToolkits(BaseFaker):

    @classmethod
    def __route(cls, locale=None):
        if locale and locale.upper() in ("ZH_CN", "CN"):
            cls.faker = cls.faker_zh
            return cls.faker
        else:
            cls.faker = cls.faker_en
            return cls.faker

    @classmethod
    def info(cls):
        locale = "zh_CN"
        name = cls.name(locale)
        email = f"{''.join([item[0] for item in pinyin(name, style=Style.NORMAL)])}@example.com"
        idcardnumber = cls.idcardnumber(locale)
        birthday = idcardnumber[6:14]
        age = cls.__current_age(datetime.strptime(birthday, "%Y%m%d"))
        gender = "男" if int(idcardnumber[-2]) % 2 else "女"
        address, postnumber = cls.address(locale)
        phonenumber = cls.faker.phone_number()

        data = {
            "name": name,
            "email": email,
            "idcardnumber": idcardnumber,
            "birthday": birthday,
            "age": age,
            "gender": gender,
            "address": address,
            "postnumber": postnumber,
            "phonenumber": phonenumber
        }
        return data

    @classmethod
    def name(cls, locale=None):
        return cls.__route(locale).name()

    @classmethod
    def email(cls, locale=None):
        return cls.__route(locale).email()

    @classmethod
    def idcardnumber(cls, locale=None):
        return cls.__route(locale).ssn()

    @classmethod
    def address(cls, locale=None):
        if locale and locale.upper() in ("ZH_CN", "CN"):
            address, postnumber = cls.__route(locale).address().split()
            return address, postnumber
        else:
            return cls.__route(locale).address()

    @classmethod
    def phone(cls, locale=None):
        return cls.__route(locale).phone_number()

    @classmethod
    def __current_age(cls, birthday: datetime):
        today = datetime.today()
        age = today.year - birthday.year

        if (today.month, today.day) < (birthday.month, birthday.day):
            age -= 1

        return age

    # def __init__(self, locale="zh_CN"):
    #     super().__init__(locale)
    #     self.fake = Faker(locale)
    #
    # def user_name(self):
    #     return self.fake.name()
    #
    # def user_email(self):
    #     return self.fake.email()
    #
    # def user_phone(self):
    #     return self.fake.phone_number()
    #
    # def user_address(self):
    #     return self.fake.address()
    #
    # def user_avatar(self):
    #     return self.fake.image_url()
    #
    # def user_id(self):
    #     return self.fake.uuid4()
