s = str("hello yuan")
print(s, type(s))
s.upper()

l = list((1, 2, 3))
l.append(4)
print(l)

d = dict({"k1": "v1"})


class Dog(object):
    # 类属性

    legs_num = 4
    has_hair = True
    has_tail = True

    def __init__(self, name, breed, color, age, weight):
        print("__init__执行")
        print("self:::", id(self))
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        self.weight = weight

    # def init_prop(self, name, breed, color, age):
    #     self.name = name
    #     self.breed = breed
    #     self.color = color
    #     self.age = age

    # 方法
    def bark(self):
        print("self:::", self)
        print(f"{self.name}正在狂吠")

    def bite(apple, person):
        print(f"{apple.name}这条狗咬{person}")

    def fetch(self):
        print(f"{self.name}捡球")

    def show_info(self):
        print(f"名字：{self.name}，品种：{self.breed}，颜色：{self.color}，年龄：{self.age}，体重：{self.weight}")


alex = Dog("李杰", "斗牛犬", "黄色", 5, 80)


# (1) 任何一个实例对象都属于本身类型
# print(alex)
# print(type(alex))
# (2) 自定义类型对象属于可变数据类型
# alex.age = 10
# print(alex.age)


# (3) 实例对象也是一等公民: 变量传递，作为函数参数，作为函数返回值

# 变量传递
# x = alex
# print(x.name)
# print(x.age)
# alex.age = 10000
# print(x.age)


# def foo(x):
#     print(x)
#     print(type(x))
#     x.append(4)

# a = 1000
# foo(a)
# b = [1, 2, 3]
# foo(b)
# print(b)


# def bar(y):
#     print(y, type(y))
#     y.age = 10000
#
#
# bar(alex)
# print(alex.age)


def test():
    peiQi = Dog("武大郎", "斗牛犬", "浅灰色", 10, 70)

    return peiQi


pq = test()
print(pq.name)
print(pq.age)
