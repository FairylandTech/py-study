class Car(object):
    # 类属性
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1

    # 实例方法
    def accelerate(self):
        print(f"一辆{self.make}的{self.model}正在加速")

# car1 = Car("Toyota", "Camry")
# car1.accelerate()
# car2 = Car("Honda", "Accord")
# print(Car.total_cars)

# 通过类对象.实例方法
# car1 = Car("Toyota", "Camry")
# Car.accelerate("apple")
