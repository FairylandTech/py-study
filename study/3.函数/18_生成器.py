#
# def func():
#     print("123")
#     return "你好"
#
#
# ret = func()
# print("得到的返回值是", ret)


# def func():   # 生成器函数
#     print(123)
#     yield "你好"   # 当函数中有yield, 该函数就是一个生成器函数, yield也有返回的意思
#
#
# gen = func()   # 生成器函数在被执行的时候. 创建生成器
# print(gen)   # <generator object func at 0x110bb1480>
# ret = gen.__next__()   # 可以让生成器函数执行到下一个yield
# print(ret)

# # 在一个生成器函数中可以有多个yield
# def func():
#     print(11)
#     yield "你好"
#     print(22)
#     yield "你不好"
#     print(33)
#     yield "你很好"
#     print("最后了. 没有了 ")
#
#
# gen = func()
# r = gen.__next__()
# print("接收到的数据", r)
#
# r2 = gen.__next__()
# print("接收到的r2", r2)
#
# r3 = gen.__next__()
# print("接收到的r3", r3)
#
# r4 = gen.__next__()  # 当程序后面没有yield之后. 此时会报错, StopIteration.
# print("接收到的r4", r4)

"""
生成器函数:
    1. 里面有yield
    2. 生成器函数在执行的时候, 实际上是创建一个生成器出来
    3. 必须使用__next__()来执行一段代码. 会自动的执行到下一个yield结束
    4. yield也是返回的意思. 可以让一个函数分段执行
    5. 当后面没有yield之后. 再次__next__会报错StopIteration
"""

# 节省内存
# 买10000件衣服
# def order():
#     lst = []
#     for i in range(10000):  # 会比较消耗资源
#         lst.append(f"衣服{i}")
#     return lst  # 列表占内存
#
#
# lst = order()
# print(lst)

# # 生成器版本
# def order():
#     for i in range(10000):
#         yield f"衣服{i}"
#
#
# g = order()
# print(g.__next__())
# # xxxxxx
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# # 改进版
# # 生成器版本
# def order():
#     lst = []
#     for i in range(10000):
#         lst.append(f"衣服{i}")
#         if len(lst) == 50:
#             yield lst
#             lst = []
#
#
# g = order()
# lst1 = g.__next__()
# print(lst1)
#
# lst1 = g.__next__()
# print(lst1)
#
# # 结论:生成器节省内存


# send()  了解.

def func():
    print("111")
    a = yield "酥饼"
    print("222", a)
    b = yield "韭菜盒子"
    print("333", b)
    yield "红酒"


g = func()
r1 = g.__next__()  # 第一次执行必须用next. 不能用send
print(r1)
r2 = g.send("哈哈")  # send给上一个yield位置传递"哈哈"
print(r2)
r3 = g.send("呵呵")
print("r3 = ", r3)

"""
__next__
send
    相同点: 可以执行到下一个yield
    不同点: send可以给上一个yield位置传值
"""

