# import master  # 模块的搜索路径, sys.path:python的环境变量
# # import sys
# # # 先找自己文件夹, 然后找项目, 最后找python
# # print(sys.path)
#
# master.func()
# print(master.name)
#
# """
# 当导入一个模块的时候, 程序会发生以下事情:
#     首先判断内存中是否已经加载了这个模块
#         如果该模块已经加载了. 那么直接把内存地址返回
#         如果没加载.
#         1. 先开辟内存. 给模块准备一个独立的名称空间
#         2. 在这个内存中运行要导入的模块
#         3. 把这个名称空间返回给import位置
# """


# import master
# import master  # 重复的导入一个模块是没有用的

# import html as html1
# from lxml import html as html2
#
# import numpy as np
#
#
# name = 123
# name = 456
# print(name)

# 不要让你自己定义的模块和系统模块或者第三方模块重名

# import json
# json.dumps()

import master
from master import func as a
a()


"""
正确的导入模块的顺序:
1. 内置模块
2. 第三方的
3. 自定义的

4. 导入的模块尽量的都写在整个文件的开头

"""


