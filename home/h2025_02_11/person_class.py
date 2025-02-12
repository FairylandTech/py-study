"""
定义-个 Person类,包含初始化 init 方法:
实例属性: 名字, name 年龄, age
1.记录由该类创建的对象的个数,创建一个对象,计数+1,删除一个对象,计数减
2.定义一个方法,可以打印当前对象的个数
3.定义一个方法 show info,输出以下信息
这是一个 Person 类,谢谢查看!
4.打卬对象的时候,可以输出打印自己的名字和年龄
我的名字是 xxx，年龄是 xxx
5.定义一个方法 study ,.输出以下信息!
我叫 xxx，我要好好学习
6.操作步骤
i.调用 show info 方法
ii.创建两个对象,打印当前对象,并打印当前的对象个数
ii. 分别使用两个对象调用 study 方法
iv. 删除一个对象,打印输出当前的对象个数
"""

class Person:

    object = 0

    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        Person.object += 1

    def number(self):
        print(Person.object)

    @classmethod
    def show_info(cls):
        print("这是一个 Person 类,谢谢查看!")

    def __str__(self):
        return f"我的名字是 {self.name}，年龄是 {self.age}"

    def study(self):
        print(f"我叫 {self.name}，我要好好学习")

    def __del__(self):
        Person.object -= 1

Person.show_info()

p1 = Person("阿道夫",22)
p2 = Person("研发",46)

print(p1)
print(p2)

p1.number()
p2.number()

p1.study()
p2.study()

p1.__del__()
p2.number()