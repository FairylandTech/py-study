# s = {"皮长山", "皮长山", "刘能"}
# print(s)

# # 去除重复
# lst = ["赵四", "尼古拉斯", "赵四", "大脚"]
# s = set(lst)
# print(s)

# # 交并差
# zhangsan = {"长白山", "三亚", "纳木错", "克拉玛依"}
# lisi = {"长白山", "纳木错", "敦煌", "成都"}
#
#
# # 求出张三和李四都去过的地方, 交集
# print(zhangsan & lisi)
#
# # 他俩一共去过哪些地方, 并集
# print(zhangsan | lisi)
#
# # 张三去过, 李四没去过的地方, 差集
# print(zhangsan - lisi)

# 集合新增数据
s = set()  # 创建set集合  {}默认是字典
s.add("克拉玛依")
s.add("新疆北部大环线")
s.add("克拉玛依")
# print(s)

# s.remove("克拉玛依")
# print(s)

# 修改: 先把要修改的内容删除, 然后新增一个新的
s.remove("克拉玛依")
s.add("楼兰古城")
print(s)


for item in s:
    print(item)



