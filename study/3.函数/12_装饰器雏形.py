# flag = False
# def login():
#     global flag
#     flag = True
#
# def add():
#     if flag:
#         # 执行新增操作
#         # 日志记录功能
#         pass
#     else:
#         print("没有登录, 请前往登录")
#
# def upd():
#     if flag:
#         # 执行新增操作
#         # 日志记录功能
#         pass
#     else:
#         print("没有登录, 请前往登录")
#
# def remove():
#     if flag:
#         # 执行新增操作
#         # 日志记录功能
#         pass
#     else:
#         print("没有登录, 请前往登录")
#
# def search():
#     if flag:
#         # 执行新增操作
#         # 日志记录功能
#         pass
#     else:
#         print("没有登录, 请前往登录")


# # 装饰器: 可以在不改变原来代码的基础上, 给函数添加新的功能
# #       可以在原有操作前面或者后面随意的添加新的功能
#
# def wrapper(fn):   # 把被装饰的函数传递进来
#     def inner():
#         print("这里是被装饰函数执行之前")
#         fn()   # 执行被装饰的函数
#         print("被装饰函数执行之后")
#     return inner  # 把内层函数返回
#
#
# def add():
#     print("我是新增函数")
#
# # a = wrapper(add)  # a就是inner
# # # a()  # 执行的是inner
# #
# #
# # add()  # 还是原来的那个样子
# # a()
#
#
# add = wrapper(add)  # 此时的add就变成了inner
# add()  # 此时执行的是inner函数



# 语法糖
def wrapper(fn):
    def inner():
        print("在执行目标函数之前")
        fn()
        print("在执行目标函数之后")
    return inner


@wrapper  # add = wrapper(add)
def add():
    print("我叫add")

# add = wrapper(add)  # 这句话可以被替代成@wrapper
add()
print(add)

# 在不改变原来函数的基础上, 给函数添加新的功能
