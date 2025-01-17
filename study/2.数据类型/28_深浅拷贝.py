"""
赋值的时候. 并没有产生新的数据, 而是对内存地址的复制
.copy() 可以产生新数据. 只是拷贝第一层内容. 浅拷贝
深拷贝, 必须使用copy模块, 会完全的复制一份

"""
import copy


# 赋值
# lst1 = ["克拉玛依", "冰糖心苹果", "羊肉串"]
# lst2 = lst1   # 并没有产生新的对象, 直接把内存地址复制了一份.
#
# print(lst1)
# print(lst2)
#
# lst1.append("葡萄干")
#
# print(lst1)
# print(lst2)
#
# print(id(lst1))
# print(id(lst2))

# 浅拷贝, 第一层
# lst1 = ["克拉玛依", "冰糖心苹果", "羊肉串"]
# lst2 = lst1.copy()  # [:]   # 产生新的列表
#
# print(lst1)
# print(lst2)
#
# lst1.append("葡萄干")
#
# print(lst1)
# print(lst2)
#
# print(id(lst1))
# print(id(lst2))


# # 浅拷贝第二层
# lst1 = ["大盘鸡", "和田玉", "口岸", ["葫芦娃", "黑猫警长"]]
# lst2 = lst1.copy()
#
# # print(id(lst1), id(lst2))
# lst1[3].append("舒克")
# print(lst1)
# print(lst2)


# # 深拷贝
# lst1 = ["大盘鸡", "和田玉", "口岸", ["葫芦娃", "黑猫警长"]]
# lst2 = copy.deepcopy(lst1)  # 深度拷贝.
#
# # print(id(lst1), id(lst2))
# lst1[3].append("舒克")
# print(lst1)
# print(lst2)
#
# print(id(lst1[3]))
# print(id(lst2[3]))


a = 10
b = a

a = 20

print(a, b)
