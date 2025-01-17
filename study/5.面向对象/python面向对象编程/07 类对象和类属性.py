class Car(object):
    # 类属性
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model

    # 实例方法
    def accelerate(self):
        print(f"一辆{self.make}的{self.model}正在加速")

# 版本1
# car1 = Car("Toyota", "Camry")
# car1.accelerate()
#  实例对象.属性 = 值 ：操作的一定是该实例空间
# car1.total_cars = 1
# print(car1.total_cars)

# car2 = Car("Honda", "Accord")
# print(car2.total_cars)

# 版本2
# Car ：类对象  调用空间存储的属性和方法
# print(id(Car))
# print(Car.total_cars)
# Car.total_cars = 1
# print(Car.total_cars)

# car1 = Car("Toyota", "Camry")
# Car.total_cars = Car.total_cars + 1
# car2 = Car("Honda", "Accord")
# Car.total_cars = Car.total_cars + 1
# print(Car.total_cars)
