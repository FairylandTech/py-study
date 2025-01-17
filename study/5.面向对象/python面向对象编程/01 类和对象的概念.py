class Dog:
    legs_num = 4
    has_hair = True
    has_tail = True

    def bark(self):
        print("狗狂吠")

    def bite(self):
        print("狗咬人")

    def fetch(self):
        print("狗捡球")


class Bird:
    legs_nums = 2
    has_wings = True
    has_teeth = False

    def fly(self):
        print("鸟飞翔")

    def eat_worms(self):
        print("鸟吃虫子")

    def nest(self):
        print("鸟筑巢")


alex = Dog()
print(alex.legs_num)
alex.bark()
alex.bite()


peiQi = Bird()
print(peiQi.has_wings)
print(peiQi.has_teeth)
peiQi.fly()


