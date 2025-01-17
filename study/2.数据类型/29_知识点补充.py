lst = ["张无忌", "张翠山", "张三丰", "张五侠"]

# # 删除所有姓张的人
# for name in lst:
#     if name.startswith('张'):
#         lst.remove(name)
#
# print(lst)  # ['张翠山', '张五侠']

# 循环列表的时候. 尽量不要删除. 否则容易删不干净

# # 把要删除的内容记录在一个新列表中,
# # 循环这个新列表, 删除老列表
# new_lst = []
# for name in lst:
#     if name.startswith("张"):
#         new_lst.append(name)
#
# for a in new_lst:
#     lst.remove(a)


# for name in lst[:]:
#     if name.startswith("张"):
#         lst.remove(name)


# 字典的删除, 在循环这个字典的时候, 删除字典中的数据. 是报错的
# dic = {"jay": "周杰伦", "55k": "卢本伟"}
# for k in dic:  # dictionary changed size during iteration
#     dic.pop(k)  # 删除


# # 把要删除的内容记录在列表中.
# # 循环列表, 删除字典
# dic = {"jay": "周杰伦", "55k": "卢本伟"}
# # 把key放在列表中
# lst = list(dic.keys())  # 拿到字典所有的key, 组装一个新列表
# for k in lst:  # 循环这个列表
#     dic.pop(k)  # 删除字典中的数据
# print(dic)

