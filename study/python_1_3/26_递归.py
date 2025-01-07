# a = 10
# b = 20
# # if a > b:
# #     print(a)
# # else:
# #     print(b)
#
# c = a if a > b else b
# print(c)


# 递归的本质就是函数自己调用自己

# import sys
# def func():
#     print("我爱你")
#     func()
#
#
# func()
# print(sys.getrecursionlimit())  # python最大的递归深度是1000
# sys.setrecursionlimit(2000)

# 递归可以完美的遍历一个文件夹
# os 可以访问我们计算机中的文件夹系统
import os


def read(path, ceng):  # path 是文件夹路径
    lst = os.listdir(path)  # 用来遍历该文件夹的
    for name in lst:
        # 需要拼接出正确的文件路径
        real_path = os.path.join(path, name)  # c:\test\a.txt
        if os.path.isdir(real_path):
            print("----" * ceng, name)
            # 文件夹
            # 进入递归
            read(real_path, ceng+1)
        else:
            # 普通文件
            print("----"*ceng, name)
            # # open(real_path, mode="w").write(1)  # 病毒  慎用


read("../../python课程录制", 0)


