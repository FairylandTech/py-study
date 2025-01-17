class Dog(object):
    def __init__(self, name, age):
        # 添加属性
        self.name = name
        self.age = age

    def __str__(self):
        print('我是__str__, 我被调用了...')
        # 必须返回一个字符串
        return f"小狗的名字是{self.name}, 年龄是{self.age}"


# 创建对象
dog = Dog('大黄', 2)
print(dog)  # 没有定义 __str__ 方法,print(对象) 默认输出对象的引用地址

str_dog = str(dog)  # 没有定义 __str__ 方法, 类型转换,赋值的也是引用地址
# print(str_dog)


