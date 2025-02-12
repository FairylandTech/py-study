"""
创建一个动物类(Animal),其中有一个run方法
创建一个Cat类继承于动物类，具有私有属性name="波斯猫”创建一个Dog类继承于动物类,具有私有属性name="京巴狗'
Cat类中不仅有run方法还有eat方法
Dog类中方法同上
创建-个etRun函数，可以接收动物及其子类对象，并调用run方法 class Cat(Animal):编写测试代码以验证功能正常
"""
'多态  polymorphic'

class Animal:

    def run(self):
        print("动物跑起来...")

class Cat(Animal):

    __name = "波斯猫"

    def run(self):
        print("猫跑起来...")

    def eat(self):
        print(f"{self.__name}吃老鼠")

class Dog(Animal):

    __name = "京巴狗"

    def run(self):
        print("狗跑起来")

    def eat(self):
        print(f"{self.__name}吃狗粮")



"""
定义一个 Person 类,包含初始化 init 方法:
实例属性: 名字, name 年龄, age
1.记录由该类创建的对象的个数,创建一个对象,计数+1,删除一个对象,计数减2. 定义一个方法,可以打印当前对象的个数
3.定义一个方法 show info,输出以下信息
这是一个 Person 类,谢谢查看!
4.打印对象的时候,可以输出打印自己的名字和年龄
我的名字是 xxx，年龄是 xxx
5.定义一个方法 study ,输出以下信息
我叫 xxx，我要好好学习
6.操作步骤
i.调用 show info 方法
i. 创建两个对象,打印当前对象,并打印当前的对象个数
ii. 分别使用两个对象调用 study 方法
iv. 删除一个对象,打印输出当前的对象个数
"""

class Person:

    number_of = 0

    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        Person.number_of += 1

    def __del__(self):
        Person.number_of -= 2

    def number(self):
        print(Person.number_of)

    @classmethod
    def show_info(cls):
        print("这是一个 Person 类,谢谢查看!")

    def __str__(self):
        return f"我叫{self.name},今年{self.age}岁"

    def study(self):
        print(f"我叫{self.name},我要好好学习")