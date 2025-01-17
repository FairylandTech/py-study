# 普通形参  缺省形参  不定长元组形参   不定长字典形参
def func(a, b=1):  # 先普通再 缺省
    pass


def func1(a, b=1, *args):  # 语法上不会报错,但是缺省参数不能使用默认值
    print('a', a)
    print('b', b)
    print(args)


def func2(a, *args, b=1):  # 普通形参  不定长元组形参  缺省形参
    print('a', a)
    print('b', b)
    print(args)


def func3(a, *args, b=1, **kwargs):  # 普通形参  不定长元组形参  缺省形参 不定长字典形参
    pass


# func1(1, 2, 3, 4)
# func2(1, 2, 3, 4)
func2(1, 2, 3, 4, b=10)


