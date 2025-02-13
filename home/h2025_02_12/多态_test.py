from home.h2025_02_12.多态 import Animal,Cat,Dog,Person
from home.h2025_02_12.多态 import Animal

a = Animal()
c = Cat()
d = Dog()

def etRun(object):
    object.run()

etRun(a)
etRun(c)
etRun(d)


Person.show_info()
p1 = Person("爱吃",22)
p2 = Person("二电厂",36)

print(p1)
print(p2)

p1.count()
p2.count()

p1.study()
p2.study()

p2.__del__()
Person.count()