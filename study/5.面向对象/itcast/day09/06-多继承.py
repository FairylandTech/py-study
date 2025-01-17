# 1. 定义Dog类, 定义bark方法,和 eat方法
class Dog(object):
    def bark(self):
        print('汪汪汪叫.....')

    def eat(self):
        print('啃骨头.....')


# 2. 定义God类, 定义 play方法和eat方法
class God(object):
    def play(self):
        print('在云中飘一会....')

    def eat(self):
        print('吃蟠桃仙丹....')


# 3. 定义XTQ类, 继承Dog类和God类
# class XTQ(Dog, God):  # XTQ 类有两个父类,这个继承关系称为多继承,XTQ类对象,可以调用两个父类中的属性和方法
class XTQ(God, Dog):  # XTQ 类有两个父类,这个继承关系称为多继承,XTQ类对象,可以调用两个父类中的属性和方法
    pass


# 4. 创建XTQ类对象
xtq = XTQ()
xtq.bark()  # 调用 Dog父类中的方法
xtq.play()  # 调用 God父类中的方法

xtq.eat()  # 两个父类都存在eat方法,子类对象调用的是 第一个父类中的方法
