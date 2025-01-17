class Potato(object):
    def __init__(self):
        self.status = '生的'
        self.total_time = 0

    def cook(self, time):
        # 计算总时间
        self.total_time += time
        # 修改地瓜的状态
        if self.total_time < 3:
            self.status = '生的'
        elif self.total_time < 6:
            self.status = '半生不熟的'
        elif self.total_time < 8:
            self.status = '熟了'
        else:
            self.status = '烤糊了'

    def __str__(self):
        return f"地瓜的状态<<{self.status}>>, 烧烤总时间为<{self.total_time}>"


# 创建对象
potato = Potato()
print(potato)
potato.cook(4)
print(potato)
potato.cook(3)
print(potato)

