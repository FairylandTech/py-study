# def func():
#     print("呵呵")
#
#
# # print(func)  # <function func at 0x10294e1e0>
# #
# # func = 20
# # print(func)
# a = func
# func()
# a()
# print(a)
# print(func)


# def func1():
# #     print("你好")
# #
# # def func2():
# #     print("你很好")
# #
# # def func3():
# #     print("你太好了")
# #
# #
# # lst = [func1, func2, func3]
# #
# # for item in lst:
# #     item()


# def func1():
#     print("呵呵")
#
# def func2():
#     print("哈哈")
#
# def func3():
#     print("吼吼")
#
# def handle(*fn): # 可以把函数作为参数传递
#     for item in fn:
#         item()
#
# handle(func1, func2, func3)


# def func():
#     def func2():
#         print("我是func2")
#     return func2   # 可以把函数作为返回值返回
#
# fn = func()
# fn()


# 闭包: 内层函数对外层函数的变量的使用
#    作用1 : 可以让一个变量被封锁起来. 外界只能看到. 但是改不了
#    作用2 : 可以让一个变量常驻内存
def func():
    a = 10  # 可以保护变量不被修改
    def inner():
        print(a)
        return a
    return inner


# fn是inner
fn = func()
b = fn()  # 函数外面访问到了函数局部变量
print(b)
fn()

"""
1. 函数名的本质就是变量名, 可以被赋值, 可以给别的变量赋值, 做参数传递, 做返回值
2. 闭包: 内层函数使用外层函数的局部变量
        1. 让一个变量能够常驻内存
        2. 保护变量不被修改. 
"""
