# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-13 20:57:46 UTC+08:00
"""


def var():
    a = 1  # int
    b = 1.1  # float
    c = "hello"  # str
    d = True  # boolean
    e = None  # 一个运行的项目中只有一个
    f = [1, 2, 3, 4, "1", 12, a, b]  # list
    g = tuple(f)  # tuple
    h = set(f)  # set
    i = {"name": 1, 1: 2, "3": f, "4": h}

    str.upper()
    str.lower()
    str.isupper()
    str.islower()
    str.isdigit()
    str.replace(" ", "")
    str.rstrip()
    str.lstrip()
    str.strip()

    str.startswith()
    str.endswith()
    str.center()

    str.rjust()
    str.ljust()

    def list_operation():
        l = []
        l.append(1)
        l.insert(3, 0)
        l.extend([2, 3])
        l.remove(1)
        l.pop(1)
        l.index(0)
        l.clear()
        l1 = l[:1]
        l2 = l[1:-1]
        l3 = l[1::2]
        l4 = l[::-1]
        l.reverse()
        l.sort()

        del l

    def tuple_operation():
        t = (1, 2, 3, 4, 5)
        t1 = t[:1]
        t2 = t[1:-1]
        t3 = t[1::2]
        t4 = t[::-1]

        del t

    def set_operation():
        a = set()

        a.add("1")
        a.add("2")
        # |, &, ^, !^

    def dict_operation():
        d = {}
        d["name"] = 1
        d.update(age=22)
        d.update({"age1": 222})

        d.keys()
        d.values()
        d.items()

        a = d["name"]
        b = d.get("name")

        d.pop("name")

        del d["age1"]

        del d


def func(a, b, c=1, *args, **kwargs):
    d = 1
    args = ()
    kwargs = {}

    def inner():
        print(d)

    return inner


def func2(func):

    def inner(*args, **kwargs):
        print("inner")
        func(*args, **kwargs)

    return inner


def func3(name):

    def func(func):

        def inner(*args, **kwargs):

            print(f"{name} inner")
            return func(*args, **kwargs)

        return inner

    return func


class A:

    c = ""
    _a = ""
    __b = ""

    def __init__(self, name):
        print("init")
        self.name = name
        self._aa = "1"
        self.__bb = "1"

    @property
    def aaac(self):
        return self.__b

    @aaac.setter
    def aaac(self, value):
        self.__b = value

    @classmethod
    def a(cls):
        print(cls._a)

    @staticmethod
    def aa():
        print("aa")

    def aaa(self):
        print(self.name)

    def __str__(self):
        return "1123"

    def __del__(self):
        print("del")


class B(A):
    def aaa(self):
        print("B")


class C(B, A):

    pass


C.mro()


def test_class(a: A):
    print(a.aaa())
