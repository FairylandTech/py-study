class Dog(object):
    def __init__(self, name, age):
        # 添加属性
        self.name = name
        self.age = age

    def __str__(self):
        # 必须返回一个字符串
        return f"小狗的名字是{self.name}, 年龄是{self.age}"

    def __del__(self):
        print(f'我是__del__ 方法,我被调用了, {self.name}被销毁了.......')


# 创建一个对象
# dog = Dog('大黄', 2)
# dog1 = Dog('小白', 1)

dog = Dog('小花', 3)  # 小花 引用计数为1
dog2 = dog   # 小花 引用计数2
print('第一次删除之前')
del dog  # dog 变量不能使用, 小花对象引用计数 1
print('第一次删除之后')
print('第二次删除之前')
del dog2  # dog2变量不能使用, 小花对象的引用计数为 0, 会立即__del__ 方法
print('第二次删除之后')

