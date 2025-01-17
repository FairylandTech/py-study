# 面试题1：如何在一个函数内部修改全局变量
# x = 1
# print(id(x))
#
#
# def foo():
#     global x
#     print(id(x))
#     x = 10
#     print(id(x))
#
# foo()
# print(x)

# 面试题2：如何修改一个enclosing变量
# x = 1
#
# def foo():
#     x = 10
#     print(id(x))
#     def bar():
#         # global x
#         nonlocal x
#         print(id(x))
#         x = 100
#
#     bar()
#     print(x)
#
#
# foo()


# 关于递归
import sys

print(sys.getrecursionlimit())


# 关于*args 和 **kwargs

# def foo(name, age, gender, *args):
#     print("args", args)

# foo("yuan", 22, "男", "180cm", "70kg")
#
# def bar(path,func,**kwargs):
#     print("kwargs",kwargs)
#
# bar("login","login",get="list")


# 关于python的函数传参是传值还是传址

# 案例1
# def foo(x):
#     print(id(x))
#     x = 20
#
#
# x = 10
# print(id(x))
# foo(x)
# print(x)

# 案例2：
def foo(x):
    print(id(x))
    # x.append(4)
    # x[0] = 100
    x = 1000


x = [1, 2, 3]
print(id(x))
foo(x)
print(x)


# 面试题： 实现一个反转整数的函数，例如 -123 --> -321

def reverse(value):
    if value > -10 and value < 10:
        return value

    value_str = str(value)

    # 正负数  -123
    # if value_str[0] != "-":
    #     ret = int(value_str[::-1])
    # else:
    #     ret = -int(value_str[1:][::-1])
    # return ret

    return int(value_str[::-1]) if value_str[0] != "-" else -int(value_str[1:][::-1])


print(reverse(234))
