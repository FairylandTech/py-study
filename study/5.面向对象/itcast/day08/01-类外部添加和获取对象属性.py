class Dog(object):
    def play(self):
        print('小狗快乐的拆家中.....')


# 创建对象
dog = Dog()
dog.play()

# 给对象添加属性  对象.属性名 = 属性值
dog.name = '大黄'  # 给dog对象添加name属性,属性值是 大黄
dog.age = 2   # 给dog对象添加age属性,属性值是 2

# 获取对象的属性值  对象.属性名
print(dog.name)
print(dog.age)

# 修改属性值 和添加一样,存在就是修改,不存在,就是添加
dog.age = 3  # age 属性已经存在,所以是修改属性值
print(dog.age)

dog1 = Dog()  # 新创建一个对象 dog1
dog1.name = '小白'
print(dog1.name)
