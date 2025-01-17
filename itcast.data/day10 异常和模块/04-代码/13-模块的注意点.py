# 自己定义的模块名字,不要和系统中你要使用的模块名字相同
import random
import sys

# 模块的搜索顺序, 当前目录  ---> 系统目录 ---> 程序报错
print(sys.path)


a = random.randint(1, 5)
print(a)


