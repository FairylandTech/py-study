"""
在需要使用父类对象的地方,也可以传入子类对象,得到不同的结果 ---- 多态
实现步骤:
1. 子类继承父类
2. 子类重写父类中的同名方法
3. 定义一个共同的方法, 参数为父类对象.在方法中调用子类和父类同名的方法
"""


# 1. 定义DOg类
class Dog(object):
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f'小狗{self.name} 在玩耍.......')


# 2. 定义哮天犬类,继承Dog类
class XTQ(Dog):
    # 3. 重写 play方法
    def play(self):
        print(f'{self.name} 在天上追云彩.....')


# 4. 定义一个共同的方法,
def play_with_dog(obj_dog):
    obj_dog.play()


# 创建Dog类对象@
dog = Dog('大黄')
play_with_dog(dog)

# 创建一个XTQ类的对象
xtq = XTQ('小黑')
play_with_dog(xtq)
