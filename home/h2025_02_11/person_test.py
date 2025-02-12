from home.h2025_02_11 import person_class
from home.h2025_02_11.person_class import Person

Person.show_info()

p1 = person_class.Person("阿道夫",22)
p2 = person_class.Person("研发",46)
print(p1)
print(p2)
p1.number()
p2.number()

p1.study()
p2.study()

p1.__del__()
p2.number()