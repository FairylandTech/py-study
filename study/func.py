# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-01-07 15:16:05 UTC+08:00
"""

from functools import wraps
import time


def func1():

    def func2():
        pass

    def func3():
        pass

    func2()
    func3()

    return 123

# 闭包: 内层函数对外层函数的变量的使用
#    作用1 : 可以让一个变量被封锁起来. 外界只能看到. 但是改不了
#    作用2 : 可以让一个变量常驻内存

def outer():
    a = 123

    def inner():
        print("inner")
        print(f"a={a}")
        return "执行inner函数完成"

    return inner


# o = outer()
# print(o, type(o))
# i = o()
# print(i, type(i))
# s = outer()()
# print(s, type(s))


def func(func):

    def a(a):
        print("start")
        r = func(a)
        print("end")

        return r

    return a

@func
def func2(a):
    print(a)
    print("func2")

# print(f"{func2(123)}")

# 通用装饰器的写法(函数)

def action(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("执行函数之前的操作")
        result =  func(*args, **kwargs)
        print("执行函数之后的操作")
        elapsed_time = time.time() - start_time
        print(f"函数{func.__name__}执行了{elapsed_time}秒")
        return result

    return wrapper

# @action
def func3(a,b):
    time.sleep(2)
    return a+b

# action(func3) = wrapper
# print(action(func3)(1,2))
# print(func3(1, 2))


# 通用装饰器带有参数的

def action2(timestamp: bool):

    def outer(func):

        def wrapper(*args, **kwargs):
            if timestamp:
                start_time = time.time()
                result = func(*args, **kwargs)
                elapsed_time = time.time() - start_time
                print(f"函数{func.__name__}执行了{elapsed_time}秒")
                return result
            else:
                print("没有timestamp")
                result = func(*args, **kwargs)
                return result


        return wrapper

    return outer



# @action2(timestamp=False)
def func4(a):
    print(a)
    time.sleep(1)
    print("func4执行完毕")
    return a

# print(func4(4))

# print(action2(timestamp=False)(func4)(1))

# @action2(timestamp=False)
# @action
def func5(a):
    print(a)
    time.sleep(1)
    return "action YES!!!"

# print(func5(2))

print(action2(timestamp=False)(action(func5))(1))

class A():

    def __init__(self, a):
        pass

    def __new__(cls, a):
        pass

    def __call__(self, *args, **kwargs):
        pass









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


# print([fibonacci(i) for i in range(1, 20)])


def factorizl(n):
    if n == 1:
        return 1
    else:
        return n * factorizl(n - 1)

# print(factorizl(5))
