"""
单继承: 如果一个类只有一个父类,把这种继承关系称为单继承
多继承: 如果一个类有多个父类,把这种继承关系称为多继承
多层继承: C--> B --> A
"""


# 1. 定义是个 动物类 animal类
class Animal(object):  # 对于Animal类和object类来说,单继承
    # 2. 在animal类书写 play方法,输出快乐的玩耍....
    def play(self):
        print('快乐的玩耍....')


# 3. 定义Dog类继承animal类,
class Dog(Animal):  # Dog --> Animal 也是单继承, Dog --> Animal --> object 这种继承关系称为多层继承
    def bark(self):
        print('汪汪汪叫.......')


# 定义类 XTQ类, 继承 Dog类
# 多层继承中,子类可以使用所有继承链中的类中的方法和属性
class XTQ(Dog):  # XTQ --> Dog 单继承, XTQ --> Dog --> Animal 类, 多层继承
    pass


xtq = XTQ()
xtq.bark()  # 调用父类Dog中的方法
xtq.play()  # 调用爷爷类 animal类中的方法
