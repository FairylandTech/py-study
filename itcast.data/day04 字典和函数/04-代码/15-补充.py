def func1(a):
    print('func1 start ... ')
    print('函数的其他代码', a)
    print('func1 end ...')


def func2(a):
    print('func2 start ....')
    a = a * a
    func1(a)  # 函数调用
    print('func2 end....')


# 调用func1()
# func1()


# 调用func2()
func2(10)


