# 定义类
class Dog(object):
    # 在类中定义的函数,称为方法, 函数的所有知识都可以使用
    def play(self):  # 暂时不管self ,
        print('小狗快乐的拆家中......')


# 创建对象 变量 = 类名()
dog = Dog()  # 创建一个对象,dog
print(id(dog))

dog1 = Dog()  # 创建一个对象 dog1
print(id(dog1))

# 可以使用对象调用类中的方法.  对象.方法名()
dog.play()
dog1.play()
