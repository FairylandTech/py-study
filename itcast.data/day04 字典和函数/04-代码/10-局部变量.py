# 局部变量, 就是在函数内部定义的变量,就是局部变量
# 局部变量,只能在函数内部使用,不能在函数外部和其他函数中使用


def func():
    # 定义局部变量 num
    num = 100
    print(num)


def func1():
    num = 200  # 这个num 和 func中的num 是没有关系的
    print(num)


# 函数调用
func()
func1()

# 探究:局部变量能否在函数外部使用
# print(num)  # 代码报错,局部变量不能在函数外部访问


