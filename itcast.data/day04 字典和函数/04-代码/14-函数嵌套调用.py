def func1():
    print('func1 start ... ')
    print('函数的其他代码')
    print('func1 end ...')


def func2():
    print('func2 start ....')
    func1()  # 函数调用
    print('func2 end....')


# 调用func1()
# func1()


# 调用func2()
func2()
