import sys


class Dog(object):
    pass


dog = Dog()  # 1
print(sys.getrefcount(dog))  # 显示的时候,会比实际的多一个,
dog1 = dog  # 2
print(sys.getrefcount(dog))  # 显示的时候,会比实际的多一个,
del dog  # 1
print(sys.getrefcount(dog1))  # 显示的时候,会比实际的多一个,
