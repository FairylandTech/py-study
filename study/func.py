# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-01-07 15:16:05 UTC+08:00
"""

from functools import wraps

a = 100


def func():
    global a
    a += 10
    print(a)


def func2():
    a = 200

    def inner():
        nonlocal a
        a = 20
        print(a)

    inner()
    print(a)


#
# func()
# func2()
# print(a)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print([fibonacci(i) for i in range(1, 20)])


def factorizl(n):
    if n == 1:
        return 1
    else:
        return n * factorizl(n - 1)

print(factorizl(5))
