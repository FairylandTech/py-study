# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-10 22:04:58 UTC+08:00
"""

"""
在python中是可以多继承的, 但是不建议使用多继承, 会导致代码的可读性变差
Java中是单继承的
C++中是多继承的

1. 重复父类方法, 不建议改父类方法中的参数和返回值类型, 如果有必要, 使用 *args 和 **kwargs
2. 在子类调用父类__init__方法, 使用super().__init__(参数)
"""


class Animal(object):

    def __init__(self, name: str):
        self.name: str = name

    def eat(self, food: str, *args, **kwargs):
        print(f"{self.name}正在吃{food}")

    def drink(self):
        print(f"{self.name}正在喝水")


class Dog(Animal):

    def __init__(self, name: str, age: int):
        self.age: int = age
        super().__init__(name)

    def __str__(self):
        return f"{self.name}, {self.age}"

    def eat(self, food: str, *args, **kwargs):
        where = kwargs.get("where", "")
        print(f"{self.name}在{where}吃{food}")

    def watch_home(self):
        print(f"{self.name}在看家")


class Cat(Animal):

    def catch_mouse(self):
        print(f"{self.name}在抓老鼠")


class Ralldoll(Cat):
    pass


class ChineseLiHua(Cat):
    pass


class H(Dog):

    def c(self):
        print(f"{self.name}在拆家")


class T(Dog):

    def ceng(self):
        print(f"{self.name}在蹭一蹭")


if __name__ == "__main__":
    dog = Dog("大黄", 2)
    dog.eat("狗粮", where="家里")
    print(dog)
