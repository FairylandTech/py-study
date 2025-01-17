class Dog(object):
    # self 作为类中方法的第一个形参,在通过对象调用方法的时候,不需要手动的传递实参值,是python解释器
    # 自动将调用该方法的对象传递给self, 所以self这个形参代表的是对象
    def play(self):
        print(f'self: {id(self)}')
        print(f'小狗 {self.name} 在快乐的拆家中.....')


# 创建对象
dog = Dog()
dog.name = '大黄'
print(f"dog : {id(dog)}")
dog.play()
print('-' * 30)
dog1 = Dog()
dog1.name = '小白'
print(f"dog1: {id(dog1)}")
dog1.play()
