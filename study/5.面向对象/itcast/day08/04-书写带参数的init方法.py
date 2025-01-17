class Dog(object):
    def __init__(self, name):  # self 是对象
        print('我是__init__方法,我被调用了')
        # 对象.属性名 = 属性值
        self.name = name

    def play(self):
        print(f"小狗{self.name}快乐的拆家中...")


# 创建对象 类名(实参值)
dog = Dog('大黄')
print(dog.name)
dog.play()
dog1 = Dog('小白')
print(dog1.name)
dog1.play()
