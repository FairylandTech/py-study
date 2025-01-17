import math


# (1) 创建一个名为 `Circle` 的类，并为其添加计算面积（area）、周长（circumference）等方法。


# class Circle(object):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return round(math.pi * self.radius * self.radius, 2)
#
#     def calculate_circumference(self):
#         return round(2 * math.pi * self.radius, 2)
#
#
# c1 = Circle(10)
# c2 = Circle(20)
#
# print(f"c1的周长{c1.calculate_circumference()},c1的面积：{c1.calculate_area()}")
# print(f"c2的周长{c2.calculate_circumference()},c2的面积：{c2.calculate_area()}")


# (2) 人狗大战


# class Person(object):
#
#     def __init__(self, name, healthy=100):
#         self.name = name
#         self.healthy = healthy
#
#     def kick_dog(self, dog):
#         print(f"{self.name}踢了{dog.name}一下")
#
#         # 狗掉血
#         dog.decrease_health(10)
#
#     def decrease_health(self, mount):
#         self.healthy -= mount
#
#
# class Dog(object):
#
#     def __init__(self, name, healthy=100):
#         self.name = name
#         self.healthy = healthy
#
#     def bite(self, person):
#         print(f"{self.name}咬了{person.name}一下")
#         # 人掉血20
#         person.decrease_health(20)
#
#     def decrease_health(self, mount):
#         self.healthy -= mount
#
#
# yuan = Person("yuan")
# alex = Dog("alex")
#
# alex.bite(yuan)
# print(yuan.healthy)
# yuan.kick_dog(alex)
# print(alex.healthy)
# yuan.kick_dog(alex)
# yuan.kick_dog(alex)
# print(alex.healthy)


# (3) 创建一个名为 `BankAccount` 的类

# class BankAccount(object):
#     def __init__(self, account_num, balance=0):
#         self.account = account_num
#         self.balance = balance
#
#     def deposit(self, mount):
#         print(f"{self.account}存款{mount}元！")
#         self.balance += mount
#
#     def withdraw(self, mount):
#
#         if self.balance >= mount:
#             self.balance -= mount
#             print(f"{self.account}取款{mount}元，当前余额：{self.balance}")
#         else:
#             print("提取金额大于余额！")
#
#     def get_balance(self):
#         # if判断
#         return self.balance
#
#
# account01 = BankAccount("123456", 10000)
# account01.deposit(20000)
# account01.withdraw(50000)
# account01.withdraw(5000)


# (4)  书籍管理

# class Book(object):
#     book_list = []
#     book_count = 0
#
#     def __init__(self, title, author, publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#
#         Book.book_list.append(self)
#         Book.book_count += 1
#
#     @classmethod
#     def show_books(cls):
#         for book in cls.book_list:
#             print(f"书籍名称:{book.title},作者{book.author},出版年份:{book.publication_year}")
#
#
# book01 = Book("西游记", "yuan", 2000)
# book02 = Book("水浒传", "rain", 3000)
# book03 = Book("三国演义", "eric", 4000)
# book04 = Book("金瓶梅", "alvin", 10000)
#
# Book.show_books()
# print(Book.book_count)


