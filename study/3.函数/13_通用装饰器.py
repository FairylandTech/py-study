# 装饰器的雏形
# def wrapper(fn):
#     def inner():
#         print("开挂")
#         fn()
#         print("关闭外挂")
#     return inner
#
#
# @wrapper
# def dnf():
#     print('我要玩儿DNF')
#
# dnf()


# # 如果被装饰的函数有参数
# def wrapper(fn):
#     def inner(*args, **kwargs):  # 任意的参数都能接受 ("大佬")
#         print("开挂")
#         fn(*args, **kwargs)  # 这里才是真正的目标函数
#         print("关闭外挂")
#     return inner
#
#
# @wrapper  # dnf = wrapper(dnf)
# def dnf(username, password):
#     print(f'登录账号为{username}, {password}, 我要玩儿DNF')
#
# @wrapper
# def wz(wx):
#     print(f"使用账号{wx}登录王者荣耀")
#
#
# # inner
# dnf("admin", "123456")  # 这里执行的是inner, inner没有参数.
# wz("大佬")


# # 如果目标函数带有返回值
# def wrapper(fn):
#     def inner():
#         print("开挂")
#         ret = fn()    # 目标函数执行之后可能会有返回值
#         print("关闭外挂")
#         return ret
#     return inner
#
#
# @wrapper
# def dnf():
#     print('我要玩儿DNF')
#     return "炙炎梵天剑"
#
# ret = dnf()  # 这里执行dnf实际上在执行inner函数
# print("我得到了一把", ret)


# 通用装饰器的写法
# def wrapper(fn):
#     def inner(*args, **kwargs):
#         """在执行目标函数之前"""
#         ret = fn(*args, **kwargs)  # 处理目标函数的返回值
#         """在执行目标函数之后"""
#         return ret
#     return inner
#
#
# @wrapper
# def target():
#     pass
#
#
# target()


# 装饰器的应用
# 写装饰器. 在执行目标函数的时候. 判断是否登录.
# 如果没有登录, 请登录, 确保用户在登录成功之后, 再执行目标
flag = False  # 默认没登录


def login_verify(fn):
    """
    这里是登录验证的装饰器
    :param fn:  被装饰的函数
    :return:   inner
    """
    def inner(*args, **kwargs):
        while 1:  # 反复的判断登录状态
            if flag:
                ret = fn(*args, **kwargs)  # 执行目标
                return ret  # 返回结果
            else:
                login()
    return inner

def login():
    global flag
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username == "admin" and password == "123456":
        flag = True
        print("登录成功")
    else:
        print("登录失败")


@login_verify
def add():
    print("我要执行新增操作")

@login_verify
def upd():
    print("我要执行修改操作")


add()
add()
upd()
upd()

# 写装饰器, 被装饰的函数被调用一次,  该函数默认执行5次
