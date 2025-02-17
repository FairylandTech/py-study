# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-12 21:42:48 UTC+08:00
"""

"""
多态是基于继承的
本质: 子类和父类都有一个同名的方法, 在调用找个方法的时候, 根据对象是什么就对象什么类中的对应方法

在需要使用父类对象的地方,也可以传入子类对象,得到不同的结果 ---- 多态
实现步骤:
1. 子类继承父类
2. 子类重写父类中的同名方法
3. 定义一个共同的方法, 参数为父类对象.在方法中调用子类和父类同名的方法
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        return f"{self.name}吃{food}, 吃饱了."


class Dog(Animal):

    def housekeeping(self):
        print("看家")

    def eat(self, food):
        return f"狗子: {self.name}吃{food}, 吃不饱."


class Cat(Animal):

    def catch_mouse(self):
        print("抓老鼠")

    def eat(self, food):
        return f"猫咪: {self.name}吃{food}, 吃不饱."


def main():
    def animal_eat(animal: Animal, foot: str):
        print(animal.eat(foot))

    dog = Dog("旺财")
    cat = Cat("Tom")
    animal_eat(dog, "骨头")
    animal_eat(cat, "鱼")


if __name__ == "__main__":
    main()
