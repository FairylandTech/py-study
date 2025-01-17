# d = {"jay": "周杰伦", "jj": "林俊杰"}

# # 添加数据
# d['key'] = "随便"   # dict[新key] = 值  新增
# print(d)

# d.setdefault("pp", "皮长山")  # key必须是不存在的
# print(d)


# # 修改
# d['jj'] = "刘能"  # dict[老key] = 值  修改
# print(d)

# # 删除
# val = d.pop('jj')
# print(d)
# print(val)
# d.clear()
#
# del d['jj']  # 参考列表


# 查询
# d = {"jay": "周杰伦", "jj": "林俊杰"}

# print(d['jay'])  # 查询, 如果key不存在, 直接报错
# print(d.get('jay', "大帅哥"))  # 查询 如果key不存在, 返回None, 没有, 空

# 特殊的
# setdefault在执行完新增流程之后. 会根据key查询value
# print(d.setdefault("jj"))

# 练习: [11,22,33,44,55,66,77,88,99]
# # 分类, 把大于50的放一起, 把小于50的放一起
# lst = [11, 22, 33, 44, 55, 66, 77, 88, 99]
# result = {}  # 结果
# # {"bigger":[66,77,88,99], "smaller":[11,22,33,44,55]}
#
# for item in lst:  # 每一个数字
#     if item > 50:
#         if result.get('bigger') == None:
#             result['bigger'] = [item]   # 没有bigger, 创建一个列表, 扔进去
#         else:
#             result['bigger'].append(item)  # 有这个列表, 添加
#     else:
#         if result.get('smaller') == None:
#             result['smaller'] = [item]   # 没有smaller, 创建一个列表, 扔进去
#         else:
#             result['smaller'].append(item)  # 有这个列表, 添加
#
# print(result)


# # 解法二
# lst = [11, 22, 33, 44, 55, 66, 77, 88, 99]
# result = {}  # 结果
#
# for item in lst:
#     if item > 50:
#         result.setdefault("bigger", []).append(item)
#     else:
#         result.setdefault("smaller", []).append(item)
# 
# print(result)

