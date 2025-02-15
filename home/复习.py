'数据类型'
from dataclasses import replace
from itertools import count

from django.contrib.admin.templatetags.admin_list import results

'字符串'

# string = '抓鸭子,抓几只'
# print(string[0::2])
# print(string[6:2:-2])
# print(string[-1::-2])
#
# cut_up = string.split(',')
# print(cut_up)
# for i in cut_up:
#     print(i)
#
# s = '鸡蛋汉堡'
# str = ' '.join(s)
# print(str)
#
# replace = string.replace(',抓几只','?下次吧')
# print(replace)
#
# string = ' Hello,Word '
# print(string.strip())
# print(string.lstrip())
# print(string.rstrip())
# print(string.upper())
# print(repr(string.lower()))
#
# import string
#
# letter = string.ascii_letters
# print(letter)
# big = string.ascii_uppercase
# print(big)
# small = string.ascii_lowercase
# print(small)
# num = string.digits
# print(num)
# punc = string.punctuation
# print(punc)



'整型'

# int1 = int(1.87)
# print(int1)
# print(divmod(10, 3))

'浮点型'
# float1 = 1.87
# print(float1)
# float_str = '2.99'
# print(type(float_str))
# print(float(float_str))
# print(type(float(float_str)))

# '列表'
# list1 = [1,2,3,4,5]
# print(list1[0::2])
#
# '列表的一些方法'
# #增
# list1.append(7)
# print(list1)
#
# list1.insert(5,6)
# print(list1)
#
# list1.extend([8,9,])
# print(list1)
# list1.extend(('aa','bb','cc'))
# print(list1)
#
# #删
# list1.pop()
# print(list1)
#
# list1.remove('aa')
# print(list1)
#
# # list1.clear()
# # print(list1)
#
# #改
# list1[9] = 10
# print(list1)
#
# print(list1.index(9)) #查找元素的索引
# print(list1.count(5))  #统计元素出现的次数
# print(len(list1))

'元组'
'元组不能增加，其他方法和列表一样'

'集合'
# set1 = {1,2,3,4,5}
# #增
# set1.add(6)
# print(set1)
#
# #删
# set1.remove(6)
# print(set1)
# set1.pop()
# print(set1)
#
# # | & ^
# set2 = {3,4,5,6,7,}
# print(set1 | set2)
# print(set1 & set2)
# print(set1 ^ set2)

'字典'
# #'1':"a",2:"b",'3':[22,33,44],'4':{'a':11,'b':22}
# dict1 = {}
#
# #增
# dict1['1'] = "a"
# dict1[2] = "b"
# dict1.update({'3':[22,33,44],'4':{'a':11,'b':22}})
# print(dict1)
# dict1.setdefault('2',111)
# print(dict1)
#
# #删
# dict1.pop('4')
# print(dict1)
#
# #改
# dict1['1'] = "aa"
# print(dict1)
# dict1.update({2:"bb"})
# print(dict1)
#
# #查
# print(dict1.get('1'))
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())


'函数'
def add(a,b):
    return a+b

'闭包'
def add_func(a):
    def add_func2(b):
        return a+b
    return add_func2
print(add_func(1)(2))

'通用装饰器，不带参数'
def decorators(func):
    def wrapper(*args, **kwargs):
        print('执行函数前')
        results = func(*args, **kwargs)
        print('执行函数后')
        return results
    return wrapper

'面向对象'

class Animal:

    race = '动物' #类属性

    def __init__(self, name, age):#初始化
        self.name = name  #实例属性
        self.age = age

    def sleep(self):  #实例方法
        print('睡觉')

    @classmethod #类方法
    def eat(cls):
        print('吃饭')

    @staticmethod #静态方法
    def drink(cls):
        print('喝水')

class Cat(Animal):

    race = '猫'

    def sleep(self):
        print('猫睡觉')

    @classmethod  # 类方法
    def eat(cls):
        print('猫吃饭')

    @staticmethod  # 静态方法
    def drink(cls):
        print('猫喝水')


def Small_cat(obj):
    obj.eat()

a = Animal('多次',18)
c = Cat('加菲猫',9)
s = Small_cat(a)
s = Small_cat(c)

