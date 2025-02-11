# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-11 21:55:09 UTC+08:00
"""


class A:
    a = "a"  # 类属性, 公有属性, 在哪里都可以访问
    _aa = "aa"  # 类属性, 受保护的属性, 在本类以及子类中可以被直接调用
    __aaa = "aaa"  # 类属性, 私有属性, 只有在本类中可以被直接调用

    def __init__(self, x, y, z):
        self.x = x  # 实例属性
        self._y = y
        self.__z = z

    def show(self):
        print(self.a)
        print(self._aa)
        print(self.__aaa)

        print(self.x)
        print(self._y)
        print(self.__z)

    @classmethod
    def get_cls_aaa(cls):
        return cls.__aaa

    def get_object_z(self):
        return self.__z

    def _a(self):
        print("_a")

    def __b(self):
        print("__b")

    def get_b(self):
        self.__b()


class B(A):

    def show(self):
        print(self.a)
        print(self._aa)
        print(self.get_cls_aaa())

        print(self.x)
        print(self._y)
        print(self.get_object_z())

        print(self._a())
        print(self.get_b())


if __name__ == "__main__":
    a = B("x", "y", "z")

    a.show()
