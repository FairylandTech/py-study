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
# print(action(func3)(1,2))     #action(func3) = wrapper(func3) = func    action(func3)(1,2) = func(1,2)
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


'''
action2(timestamp=False) = outer    
action2(timestamp=False)(func4) = outer(func4) = func    
action2(timestamp=False)(func4)(1) = outer(func4)(1) = func(1)
'''

# print(action2(timestamp=False)(func4)(1))

# @action2(timestamp=False)
# @action
def func5(a):
    print(a)
    time.sleep(1)
    return "action YES!!!"

# print(func5(2))

'''
action2(timestamp=False) = outer 
action2(timestamp=False)(action) = outer(action)

action(func5) = wrapper() = func   action(func5))(1) = func(1)
action2(timestamp=False)(action(func5)) = outer(action(func5)) = outer(wrapper()) = outer(func) = wrapper
action2(timestamp=False)(action(func5))(1) = outer(action(func5)(1) = outer(wrapper()(1)) = 
'''

print(action2(timestamp=False)(action(func5))(1))

'''
print(action2(timestamp=False)(action(func5))(1))
action2(timestamp=False)(action(func5))(1)
(action(func5))(1)
action(func5)(1)
'''


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

import time
from functools import wraps

def rate_limiter(seconds):
    def decorator(func):
        last_called = [0]  # 使用列表以便在闭包中修改

        def wrapper(*args, **kwargs):
            current_time = time.time()
            if current_time - last_called[0] < seconds:
                print(f"警告: 函数 {func.__name__} 被调用的频率过高，请等待 {seconds - (current_time - last_called[0]):.2f} 秒再试。")
            else:
                last_called[0] = current_time
                return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limiter(5)
def my_function():
    print("函数执行成功！")

# 测试代码
my_function()  # 第一次调用，正常执行
time.sleep(2)
my_function()  # 第二次调用，应该打印警告
time.sleep(5)
my_function()  # 第三次调用，正常执行
