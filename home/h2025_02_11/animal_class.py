"""
创建一个动物(Animal)的基类,其中有一个run方法, 输出跑起来....
创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法run方法输出跑起来....
eat 方法输出马吃东西...
创建一个Donkey（驴）类继承于动物类，Donkey类中不仅有run方法还有eat方法run方法输出跑起来....
eat 方法输出驴吃东西...
创建一个Mule（骡子）类继承于Horse，Donkey，初始化name为 骡子。 问题: 创建 Mule 类的对象, 调用 eat 方法,调用的是哪个父类中的方法?
"""
class Animal:

    def run(self):
        print("跑起来....")

class Horse(Animal):

    def eat(self):
        print("马吃东西...")

class Donkey(Animal):

    def eat(self):
        print("驴吃东西...")

class Mule(Horse, Donkey):

    def __init__(self,name):
        self.name = name

