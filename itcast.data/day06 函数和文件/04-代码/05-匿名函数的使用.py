def my_calc(a, b, func):
    """
    进行四则运算
    :param a: 第一个数据
    :param b: 第二个数据
    :param func: 函数,要进行的运算
    :return: 运算的结果
    """
    print('其他的函数代码...')
    num = func(a, b)
    print(num)


def add(a, b):
    return a + b


# 调用
my_calc(10, 20, add)
my_calc(10, 20, lambda a, b: a - b)
my_calc(10, 20, lambda a, b: a * b)
my_calc(10, 20, lambda a, b: a / b)


