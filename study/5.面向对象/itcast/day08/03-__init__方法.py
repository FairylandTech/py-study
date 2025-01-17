class Dog(object):
    def __init__(self):  # self 是对象
        print('我是__init__方法,我被调用了')
        # 对象.属性名 = 属性值
        self.name = '小狗'


# 创建对象
# Dog()
dog = Dog()
print(dog.name)
dog1 = Dog()
print(dog1.name)
