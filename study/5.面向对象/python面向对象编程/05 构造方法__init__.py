# 声明类
class Dog:
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


# 版本1
# alex = Dog()
#
# alex.init_prop("李杰", "斗牛犬", "黄色", 5)
#
# alex.bark()
# alex.show_info()
#
# peiQi = Dog()
# peiQi.init_prop("武大郎", "斗牛犬", "浅灰色", 10)
#
# peiQi.bark()
# peiQi.show_info()


# 版本2
"""
类实例化步骤
(1) 开辟实例空间
(2) 调用__init__(实例空间地址)
(3) 将实例空间地址作为类的实例子化的返回值

"""
alex = Dog("李杰", "斗牛犬", "黄色", 5, 60)
print("alex:::", id(alex))
# peiQi = Dog()


peiQi = Dog("武大郎", "斗牛犬", "浅灰色", 10, 70)
print("peiQi:::", id(peiQi))

peiQi.show_info()