class Cars(object):
    # 类属性
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        print("self.__class__:",id(self.__class__))
        self.__class__.total_cars += 1

    # 实例方法
    def accelerate(self):
        print(f"一辆{self.make}的{self.model}正在加速")

    @classmethod
    def show_total_cars(cls):
        print(id(cls))
        print(f"当前的total_cars：{cls.total_cars}")


# print(Car.total_cars)
# car1 = Car("Toyota", "Camry")
# car1.show_total_cars()
print(id(Cars))
Cars.show_total_cars()


car1 = Cars("Toyota", "Camry")

Cars.show_total_cars()
