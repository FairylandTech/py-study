class Potato(object):
    def __init__(self):
        self.status = '生的'
        self.total_time = 0
        self.name_list = []  # 保存调料的

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
        # buf_list = str(self.name_list)  # str([])  ===> '[]'
        # buf_list = buf_list.replace('[', '')
        # 字符串.join(列表), 将字符串添加到列表中的每个元素之间,组成新的字符串
        buf = ','.join(self.name_list)
        if self.name_list:
            return f"地瓜的状态<<{self.status}>>, 烧烤总时间为<{self.total_time}>, 调料有: {buf}"
        else:
            return f"地瓜的状态<<{self.status}>>, 烧烤总时间为<{self.total_time}>,还没有添加调料"

    def add(self, name):
        self.name_list.append(name)


# 创建对象
potato = Potato()
print(potato)
potato.add('油')
potato.cook(4)
potato.add('辣椒面')
print(potato)
potato.cook(3)
potato.add('孜然')
print(potato)

