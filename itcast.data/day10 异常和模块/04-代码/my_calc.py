def add(a, b):
    print(a + b)


if __name__ == '__main__':
    add(10, 20)
    # __name__ 变量,在每个模块即代码文件中都有,是系统自己定义的
    # 1. 直接运行当前代码, 值为 __main__
    # 2. 把文件作为模块导入时,运行,结果是 my_calc(文件名)
    print(__name__)

