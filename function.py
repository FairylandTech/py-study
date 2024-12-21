# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-12-19 22:32:45 UTC+08:00
"""

"""
定义函数关键字: def
函数名: add
参数: a, b, 位置参数: a, b
可变参数: *args, **kwargs
args: 位置参数, 元组
kwargs: 关键字参数, 字典

函数作用域: 函数内部, 函数外部
"""


# def add(a, b, *args, **kwargs):  # 函数定义, a,b 是形参
#     # 函数体
#     def sub_add():
#         def subsubadd():
#             a1 = 34
#             print(a1 + a2)
#
#         print(a1 + a2)
#         subsubadd()
#
#     a1 = args[0]
#     a2 = args[1]
#
#     print(args)
#     print(a1, a2)
#
#     print(kwargs)
#     print(kwargs.get("name"))
#     print(kwargs.get("age"))
#     print("add", a + b)
#     sub_add()
#     return a + b  # 返回值
#
#
# print(add(1, 2, 2, 3, name="alice", age=12))


# 1    [竞赛入门]简单的a+b  ------------------------------------
# def ab(a,b):
#
#     print(a+b)
#
# while True:
#     a = int(input("请输入a的值:"))
#     b = int(input("请输入b的值:"))
#     ab(a,b)


#     [编程入门]第一个HelloWorld程序------------------------------
# print('*'*20)
# print("Hello World")
# print('*'*20)


##     [编程入门]三个数最大值----------------------------------
# a = int(input("请输入a的值:"))
# b = int(input("请输入b的值:"))
# c = int(input("请输入c的值:"))
# l = [a,b,c]
# print(max(l))
# a = input("请输入三个数:")
# print(max(a.split()))


# [编程入门]  密码破译--------------------------------------
# a = input("请输入需要加密的单词:")
# import string
# mapping_str = string.ascii_letters
# # enumerate 和 range
# mapping = {key: index for index, key in enumerate(mapping_str)}
# print("".join([mapping_str[mapping.get(i) + 4] for i in a]))
# #
# a = input("请输入需要加密的单词:")
# import string
# M = string.ascii_letters
# jia_mi = ''
# for i in a:
#     num = M.find(i)
#     j = M[M.find(i)+4]
#     jia_mi = jia_mi + j
# print(jia_mi)


# print(M)
# print(type(M))

# M = "abcdefghijklmnopqrstuvwxyz"
# a = "dh"
# for i in a:
#     num =M.find(i)
#     print(num)
#     print(type(num))
# print(M[3])

# 题目 1005: [编程入门]温度转换------------------------------
# a = float(input("请输入一个华氏温度值:"))
# a1 = round(a,2)
# print(a1)
#
# t =5*(50.23 - 30)/9
# print(round(t,2))
# print("摄氏温度值为:",t)
# c = 15.2344
# print(type(c))
# print(round(c,2))


# lambda 匿名函数

def add(a, b):
    return a + b


# print(add(1, 2))
# print((lambda a, b: a + 1 if a <= 1 else a ** b)(2, 2))
# lambda 参数(有几个参数就用逗号隔开): 返回值

# global
import copy
import math

# build-in function
print(math.pi)
print(math.e)

"""
禁止数字开头或者符号开头
模块  # .py 文件, 规范: 一个单词(名词), 如果不够, 使用下划线分割, 全部小写
包  # 一个带有__init__.py的文件夹, 规范: 一个单词(名词), 如果不够, 使用下划线分割, 全部小写  __all__
类  # 关键字 class, 规范: 大驼峰(名词)
函数  # 关键之 def, 规范: 一个单词(动词), 如果不够, 使用下划线分割(起码有一个动词), 全部小写
对象  # (instance) 规范: 一个单词(名词), 如果不够, 使用下划线分割, 全部小写
全局变量  # 规范: 一个单词(名词), 如果不够, 使用下划线分割, 全部大写
局部变量  # 规范: 一个单词(名词), 如果不够, 使用下划线分割, 全部小写
类属性  # 规范: 一个单词(名词), 如果不够, 使用下划线分割, 全部小写/大写
实例属性  # 规范: 一个单词(名词), 如果不够, 使用下划线分割, 全部小写/大写
静态方法  # 关键字: @staticmethod, def 规范: 一个单词(动词), 如果不够, 使用下划线分割(起码有一个动词), 全部小写
类方式   # 关键字: @classmethod, def 规范: 一个单词(动词), 如果不够, 使用下划线分割(起码有一个动词), 全部小写
实例方法  # def 规范: 一个单词(动词), 如果不够, 使用下划线分割(起码有一个动词), 全部小写

在脚本中, 如何触发main()
if __name__ == '__main__':

python 每一行应该有多少个字符: 79 / 150
python代码格式化工具: black # pip install black
python函数最多有多少个if或者for: 15
python函数最多有多少个参数: 255, 建议小于9
class 上空2行
def 上空1行
import导入顺序: 标准库, 第三方库, 自定义库
main()和函数/类之间空2行
"""

"""
ClassRome  # 大驼峰 
classRome  # 小驼峰
class_room  # 全小写下划线分割
CLASS_ROME  # 全大写下划线分割
class-room  # 连字符分割
"""

A = 1


def add1():
    A = 2
    print(f"add1: {A}")

    def add2(a=None):
        c = 2
        if not a:
            global A
            a = copy.deepcopy(A)

        return a + 1

    return add2()


print(add1())


print(range(10))

a = "123456"

print(a[slice(0,2)])
print(a[:2])

import this
