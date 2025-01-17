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


class Cat(object):
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f'小猫{self.name} 被撸中...')


# 4. 定义一个共同的方法,
def play_with_dog(obj_dog):
    obj_dog.play()


# 创建Dog类对象@
dog = Dog('大黄')
play_with_dog(dog)

# 创建一个XTQ类的对象
xtq = XTQ('小黑')
play_with_dog(xtq)


cat = Cat('小花')
play_with_dog(cat)