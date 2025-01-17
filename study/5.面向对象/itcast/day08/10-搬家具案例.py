# 定义家具类 Furniture 类
class Furniture(object):
    def __init__(self, name, area):
        # 类型
        self.name = name
        # 面积
        self.area = area

    def __str__(self):
        return f'家具的类型<{self.name}>, 占地面积<{self.area}>平'


# 定义房子类
class House(object):
    def __init__(self, address, area):
        self.address = address
        self.h_area = area
        self.furniture_list = []
        self.free_area = area  # 房子的剩余面积

    def add_furniture(self, obj_furniture):
        """ 添加家具 obj_furniture:  家具类的对象"""
        if self.free_area > obj_furniture.area:
            self.furniture_list.append(obj_furniture)
            # 修改剩余面积
            self.free_area -= obj_furniture.area
            print(f'家具<{obj_furniture.name}>添加成功')
        else:
            print('添加失败,换个大房子吧')

    def __str__(self):
        return f"房子的地址为<{self.address}>, 占地面积为<{self.h_area}>, 剩余面积为{self.free_area}"


# 创建家具对象
bed = Furniture('豪华双人床', 15)
print(bed)

# 创建一个房子类对象
house = House('意大利农场', 100)
print(house)
house.add_furniture(bed)
print(house)

