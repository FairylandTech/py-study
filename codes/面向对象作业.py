# coding=utf-8


class Star:

    def __init__(self, name, film):
        self.name = name
        self.film = film

    def playing(self):
        print(f"{self.name}出演了{self.film}, 非常好看")

    def __str__(self):
        return f"{self.name}是我的偶像, 我非常喜欢他的电影{self.film}"

    def __del__(self):
        print(f"我不喜欢{self.name}了")


class Person:
    __count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.__count += 1

    @classmethod
    def get_object_count(cls):
        print(cls.__count)

    def __str__(self):
        return f"我的名字是{self.name}, 年龄是{self.age}"

    def study(self):
        print(f"我叫{self.name}, 我要好好学习")

    @staticmethod
    def show_info():
        print("这是一个Person类, 谢谢查看")

    def __del__(self):
        Person.__count -= 1


if __name__ == "__main__":
    # stats = {}
    # for i in range(5):
    #     name = input("请输入明星名字: ")
    #     film = input("请输入明星电影: ")
    #     stats.update({name: film})
    #
    # for name, film in stats.items():
    #     star = Star(name, film)
    #     star.playing()
    #     print(star)
    Person.show_info()

    p1 = Person("Tom", 18)
    p2 = Person("Jerry", 20)
    print(p1)
    print(p2)

    Person.get_object_count()

    p1.study()
    p2.study()

    del p2

    Person.get_object_count()
