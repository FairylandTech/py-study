my_list = ['hello', 'python', 'cpp']   # 列表中存储了三个字符串对象

print(my_list)


class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'

    def __repr__(self):
        """repr 方法和 str 方法,非常类似,也是必须返回一个字符串"""
        return f"{self.name}"


# 将三个Dog类的对象添加到列表中
my_list1 = [Dog('大黄', 2), Dog('小白', 4), Dog('小花', 6)]
print(my_list1)

dog = Dog('大黄', 2)
print(dog)   # __str__

