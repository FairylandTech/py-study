# coding=UTF-8

import time

"""
类是具体代指一类事物的(泛型), 没有明确指一类或一种东西 (抽象的概念)

类的名词:
关键字: class
类名, class 后的
实例属性
实例方法
类属性
类方法
静态方法

封装
继承
多态

关于一下写法的:
以__开头, __结尾的是类中的特殊方法(__init__, __new__, __str__, __repr__, __iter__, __del__, __dict__, __int__, __eq__, ...), 个人需求不建议用 这种方式命名

以_/__开头的方法/属性为私有方法/属性, 如果使用 classmethod/staticmethod 同样适用, 外部不可以被调用
1. 以_开头的子类可以调用, 可以被重写
2. 以__开头的子类不可调用(只有该类可以调用), 可以被重写

了解:
单例模式: 在整个项目/整个代码中, 该类只可以实例化一次(只有一个对象)
工具类: 数据库的连接, redis的连接, 日志, ...

复习:
普通函数传参顺序: 普通形参, 位置参数, 带有默认值, 关键字参数, (name, age, *args, gender="男", **kwargs)
"""


class Dog:  # 类名: Dog, 在python中所有的类全部继承于Object->type(元类(MetaClass))
    classname = "Dog Class"  # 类属性
    
    def __init__(self, name):  # 构造函数(在类被实例化的时候调用), name: 实例属性(实例属性在什么时候传: 在实例化的时候穿)
        print(f"构造了一个{name}对象")
        self.name = name

    def eat(self, foot):  # 实例方法: 第一个参数必须是实例化后的对象, self: 实例化后的对象, 后面的传参方式和普通函数一样, 调用: 实例对象.实例方法()
        print(f"{self.name}正在吃{foot}")

    @classmethod
    def skills(cls):  # 类方法, 第一个参数是类本身, cls: 类本身, 调用: 类名.类方法(), 实例对象.类方法()
        print(f"{cls.classname}的技能: [吃饭, 睡觉, 陪伴主人]")

    @staticmethod
    def run():  # 静态方法, 只是写在类里, 和普通函数一样, 调用: 类名.静态方法名()
        print("狗狗在跑步")

    def __str__(self):  # 在构造了一个对象后, 直接print打印这个对象的时候会默认调用__str__()方法, 给人看的
        """
        注意: __str__(), 有且只有一个参数: self: 这个对象, 返回指必须是str类型的
        """
        return f"{self.name}: wow(str)"

    def __del__(self):  # 当前没有这个对象的引用时候会自动调用__del__()方法
        print("Dog被销毁了")



# dog1 = Dog("dog1")  # 类名() -> 构造对象(实例化, 实例化这个类为一个具体的对象), dog1 就是一个具体的对象
# print(dog1)
# dog2 = Dog("dog2")

# 获取实例属性/实例方法的时候只能通过 对象.属性名/对象.实例方法名
# print(dog1.name)  # 获取实例属性, 对象.属性名
# dog1.name = "大黄"  # 修改实例属性 name = "大黄"
# dog1.eat("狗粮")

# print(dog2.name)

# print(Dog.classname)
# Dog.classname = "狗类"  # 修改类属性 classname = "狗类"
# print(Dog.classname)
# Dog.skills()

# 写 classmethod 和 staticmethod, 调用方式都是一样的, 在实际中到底改用哪一个
# 使用 classmethod 装饰后方法的第一个参数是这个类本身, 如果需要用类属性就是用 classmethod
# 如果单纯的是一个方法, 和普通函数一样, 不涉及和这个类有任何管理, 也不用这个类中的属性, 或者其他的方法, 只是单纯的放在这个类中作为一个普通的函数来调用的, 就使用 staticmethod 装饰器
# 建议写类方法, 但是还是要根据实际需求来


class Potato:

    def __init__(self, name):
        self.__name = name
        self.time = 0
        self.status = "生的"

    def cook(self, time):
        if not isinstance(time, (int, float)):
            raise RuntimeError("参数只是是int/float")
        if time < 0:
            raise RuntimeError("参数必须大于0")

        self.time += time

        if self.time <= 4:
            self.status = "生的(不熟)"
        elif 5 <= self.time < 10:
            self.status = "烤熟了"
        elif self.time >= 10:
            self.status = "烤黑了, 糊了..."

    def __str__(self):
        return f"{self.__name}地瓜: 烤了{self.time}分钟, {self.status}"

p1 = Potato("小土豆")
p1.cook(2)
print(p1)
p1.cook(2)
print(p1)
p1.cook(2)
print(p1)

p2 = Potato("大番薯")
p2.cook(10)
print(p2)
