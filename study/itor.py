# coding=UTF-8
from Tools.scripts.pysource import binary_re


# 生成器, 关键字: yield


def generate_number(number: int):
    for i in range(number):
        yield i


def get_data():
    # result = []
    # ..... 获取数据的代码
    for i in range(10):
        # result.append(i)
        yield i
    # return result

data = get_data()  # 如果 get_data() 获取的数据很多, 几百万/几千万数据 内存就会变大, 使用生成器
print(data, type(data))

for item in get_data():
    print(item)


a = 1
da = a if a == 1 else None  # 三元表达式, 含义: 如果 a == 1 就返回 if 之前的, 如果不等于 就返回 else 之后的
print(da)

for i in range(10): print(i) if i % 2 == 0 else print(None)