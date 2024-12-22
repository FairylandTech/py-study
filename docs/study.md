解释性语言, 在win中可以被编译为pyd, 在unix中可以被编译为so/pyo, pyc文件是py的二进制文件, 在执行py脚本时, 会以脚本的当前路径为根路径生产``__pycache__`的文件夹, 里面就是pyc二进制文件



python 各个版本有出入

python2.7, python3.6.3, python3.8, python3.9, python3.11



开发IDEA: pycharm, IDEA, vscode, vs



脚本/项目, 都有两类方式, 面向对象(复用性高), 函数式(简单, 逻辑通透)



python的运行方式, 只有一个主入口, 而且一定要注意导包(建议 `from ... import ...`)



python包: 文件夹形式, 但是这个文件夹中又`__init__.py`的文件叫python的包, 没有py文件的叫`目录`

python模块: 一个py文件就是一个模块



python的解释器和虚拟环境

pip: python的包管理工具(第三方包管理) `https://pypi.com`

pipenv, venv, pipreq, toml

科学计算: Anaconda, MiniAnaconda



基础模块:

```python
import os
import sys
import shutil
import subprocess
import math
import time
import datetime
import json

import yaml

import requests

import pandas as pd
import numpy as np
```







数据类型：

```python
# python的数据类型
# 1. str   字符串  String  (python3) / python2: python2中的unicode=python3的str, python2中的str=python3的bytes
# 2. bytes 二进制  Byte
# 3. list  列表   Array
# 4. tuple 元组
# 5. int   整型   int
# 6. float 浮点   double/float
# 7. dict  字典   HashMap
# 8. set   集合
# 9. boolean 布尔值 0->Flase, 1->True
# -- 不常见的
# array, bytearray, dequn, OrderedDict, Counter, namedtuple

# from array import array
# 双向队列 / 有序字典(本来python2中的字典是无序的, 但是python3是看起来有序的) / 计数器 / 命名元组
# from collections import deque, OrderedDict, Counter, namedtuple
# deque: 双向队列
# 二进制数组
# bytearray()
# import pandas as pd
## pd.DataFrame()
```

一，字符串

字符串的一些常用方法：

```python
字符串.strip()										#去掉两边的空格
字符串.rstrip()									# 去掉右边的空格
字符串.lstrip()									# 去掉左边的空格
字符串.upper()										#将内容全部转换为大写
字符串.lower()										#将内容全部转换为小写
字符串.replace("被替换的内容", "需要替换的内容")		# 替换空格
字符串.join(内容，常见用for循环遍历将内容拼接)		#	
字符串.spilit('分割标识')							#以什么什么为分割，分割成了几部分，就是几个字符串（拆包）
repr(字符串)										#显示原生字符串，带引号的

##一个常用的模块
import string

letters = string.ascii_letters					#所有的英文字母，包括大小写
lowercase = string.ascii_lowercase				#所有的小写字母
uppercase = string.ascii_uppercase				#所有的大写字母
digits = string.digits							#所有的数字


##例子
s = "  jkfjj字  "
s1 = "    aq Qa qf 天 字符串 "
s2 = "好好学习,天天向上"
print(repr(s.strip()))
print(repr(s.upper()))
print(repr(s1.upper()))
print(repr(s.lower()))
print(repr(s1.lower()))

a = "  aa aa abcd我的 a   a   a     "
print(a.strip())  # 去掉两边的空格
print(a.rstrip())  # 去掉右边的空格
print(a.lstrip())  # 去掉左边的空格
print(a.replace(" ", ""))  # 替换空格

print(repr("".join(item for item in s1 if item != " ")))
a1 = ""
for i in a.split(" "):
    if i != " ":
        a1 += i

print(a1)
```



二，整型，浮点型

```python
1. 定义一个整型
int1 = int()  # 默认值为0, if判断为False(带有not)
int2 = 1
int3 = -1

# print(int1)
# print(int2)
# print(int3)

# 运算 + - * / ** %(取模)
print(int(10 / 3))
# print(divmod(10, 2))			#divmod(10, 2)计算10除2的整除和取余
```



三，列表，元组，集合

字符串
整型, 浮点
列表, 元组, 集合  -- 容器
字典

```python
特性:
    1. 列表:
            可变的(可以向容器内添加/删除/替换元素)
            有序的(在内存中是有顺序的, 可以切片, 可以根据索引取值)  __index__()
            可重复的(同一个元素可以重复出现多次)
            可迭代的(容器本身就是一个迭代器类型的对象, 可以for循环) __iter__()
            可以存任意数据类型(在python中所有的数据类型都可以存)
    2. 元组:
            不可变的
            有序的(在内存中是有顺序的, 可以切片, 可以根据索引取值)
            可重复的(同一个元素可以重复出现多次)
            可迭代的(容器本身就是一个迭代器类型的对象, 可以for循环) 
            可以存任意数据类型(在python中所有的数据类型都可以存)
    3. 集合:
            可变的(可以向容器内添加/删除/替换元素)
            无序的
            不可重复的
            可迭代的(容器本身就是一个迭代器类型的对象, 可以for循环)
            ** 有限的数据类型(单一的数据类型)
```

初始化列表，元组，集合

```python
list1 = list()  # 默认值: []
tuple1 = tuple()  # 默认值: ()
set1 = set()  # 默认值: {}

list2 = []
tuple2 = ()
set3 = set()
# ** 初始化 set(集合) 只能用 set(), 或者 {1, 2, 3}
```



列表，常用方法

```python
import string

list_test = [i for i in string.ascii_lowercase]

# 1. 添加元素
# append 默认加在后面. 参数是元素
list_test.append("1")  # 时间复杂度O(1)
# extend 默认加在后面, 参数是一个容器(可迭代的对象)
list_test.extend([i for i in str(string.digits)])
# insert 参数1: 索引, 参数2: 元素, 把元素插入到指定的索引位置
list_test.insert(0, "111")  # 时间复杂度O(n)

# 2. 删除元素
# pop 默认删除最后一个元素, 参数是索引, 删除指定索引位置的元素
list_test.pop()  # 时间复杂度O(1)
del list_test[2]  # 时间复杂度O(1)
# remove 参数是元素, 删除指定的元素
list_test.remove("111")  # 时间复杂度O(n)
# clear 清空列表
# list_test.clear()
# del list_test

# 3. 修改元素
list_test[len(list_test) - 1] = 111  # 时间复杂度O(1)

# 4. 查找元素
# index 参数是元素, 返回索引
print(list_test.index("0"))
# count 参数是元素, 返回元素出现的次数
print(list_test.count(1))
# 切片
print(list_test[0:5])
print(list_test[0:6:2])
print(list_test[:6:2])
print(list_test[20::5])
print(list_test[20::-1])
print(list_test[2::-3])

# print(list_test)
```



元组

```python
#因为元组是不可变类型，所以没有增加，删除，修改的方法，只有查询的方法

tuple_test = (1, 2, 3, 4)
#print(tuple_test[0])

ccc = [0, 1]
#print(ccc[0])
#print(ccc.__getitem__(0))
```



字典

```python
# 字典 HashMap 哈希表, key-value
from collections import OrderedDict

dict_test1 = dict()
dict_test2 = OrderedDict()
dict_test = {"key1": "value1", (1, 2): "asd", 1: "1", 1.3: "1.3"}
# 问题1: dict 的 key 必须是可哈希的(不可变的数据类型就一定是可哈希的)数据类型, 不能是可变的数据类型: tuple, str, int, float
from typing import Any
# 问题2: dict 的 value 可以是任意类型 Any
# 问题3: dict 的 key 不可重复, 重复就代表update

# 字典常用方法
# 1. 添加元素
key3 = "key3.1"
dict_test["key2"] = "value222222222222"
dict_test.update(key3="key3")
dict_test.update({key3: "value3"})
# update 的坑
key4 = "key4.4"
dict_test.update(key4=123)			#这里的字典是{"key4":123}  --  *=*的方式直接给字典里写入数据
dict_test.update({key4: 1234})		#这里的字典是{'key4.4': 1234}  --上面有了key4这个变量，先将key4的变量值作为键值给到字典的键，再将冒号后的值存入字典

# 删除
# del dict_test
del dict_test["key1"]  # 删除
values = dict_test.pop("key2")  # 删除 参数 key的名称, 返回值是已经删除的key对应的value
#print(values)
# 查询
print(dict_test["key3.1"])
print(dict_test.get("key3.1"))

# 查询所有的key
print(dict_test.keys())  # 返回一个可迭代的对象
# 查询所有的values
print(dict_test.values())  # 返回一个可迭代的对象
# 查询所有的key-value
print(dict_test.items())  # 返回一个可迭代的对象, 但是需要解包(在for循环中使用)
 for key, value in dict_test.items():
     print(key, value)


print(dict_test)
```









