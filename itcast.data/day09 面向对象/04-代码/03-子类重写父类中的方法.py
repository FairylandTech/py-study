# 1. 定义Dog类, 书写bark方法, 输出 汪汪汪叫
class Dog(object):
    def bark(self):
        print('汪汪汪叫.........')


# 2. 定义XTQ类,继承Dog类. 重写父类中的bark方法, 输出 嗷嗷嗷叫
class XTQ(Dog):
    def bark(self):
        print('嗷嗷嗷叫--------')


# 创建Dog类对象
dog = Dog()
dog.bark()  # 父类自己的

# 创建XTQ类对象
xtq = XTQ()
xtq.bark()
