"""
实例方法: 类中默认定义的方法,就是实例方法, 第一个参数为self,表示实例对象
类方法: 使用 @classmethod 装饰的方法,称为类方法, 第一个参数是cls,代表的是类对象自己
静态方法: 使用 @staticmethod 装饰的方法,称为静态方法, 对参数没有特殊要求,可以有,可以没有
什么情况定义为实例方法,什么情况定义为类方法, 什么情况下静态方法?
1. 如果在方法中使用了实例属性, 那么该方法必须定义为实例方法
2. 前提:不需要使用实例属性. 需要使用类属性,可以将这个方法定义为类方法
3. 前提:不需要使用实例属性,同时也不需要使用类属性, 此时可以将这个方法定义为静态方法
"""


class Dog(object):
    class_name = '狗类'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):  # 实例方法
        print(f"小狗{self.name} 在快乐的玩耍....")

    @staticmethod  # 定义静态方法
    def show_info():
        print('这是一个Dog类')


dog = Dog('大黄', 2)
dog.play()
# 对象.方法名()
dog.show_info()
# 类名.方法名()
Dog.show_info()
