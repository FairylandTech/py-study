# 在python中,定义类使用关键字 class , 语法如下
"""
# object 是所有的类基类,即最初始的类
# 类名: 遵循大驼峰的命名规范
class 类名(object):
    类中的代码
"""


# 定义方式一, 推荐
class Dog(object):
    pass


# 定义方式二
class Dog1():   # 括号中的内容可以不写
    pass


# 定义方式三
class Dog2:   # 括号也可以不写
    pass


"""
新式类: 直接或者间接继承object的类, 在python3中,所有的类默认继承object类,即python3中所有的类都是新式类
旧式类(经典类): 已经过时,不推荐使用
"""