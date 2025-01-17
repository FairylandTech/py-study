# 1. 定义是个 动物类 animal类
class Animal(object):
    # 2. 在animal类书写 play方法,输出快乐的玩耍....
    def play(self):
        print('快乐的玩耍....')


# 3. 定义Dog类继承animal类,
class Dog(Animal):
    pass


# 4. 创建dog类对象.调用父类的方法
dog = Dog()
dog.play()
