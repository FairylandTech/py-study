# 1. 定义Dog类
class Dog(object):
    def __init__(self, name):
        # 添加属性
        self.age = 0
        self.name = name

    def __str__(self):
        return f'名字为:{self.name}, 年龄为{self.age}'


# 2. 定义XTQ类继承Dog类
class XTQ(Dog):
    # 子类重写了父类的__init__ 方法,默认不再调用父类的init方法, 需要手动的调用父类的init方法
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def __str__(self):
        return f'名字为:{self.name}, 年龄为{self.age}, 毛色为:{self.color}'


# 3. 创建XTQ类对象
xtq = XTQ('小黑', '红色')
print(xtq)
