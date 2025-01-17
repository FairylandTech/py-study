# 案例1
# l = [1, 2, 3, 4, 5]
# new_l = []
# for i in l:
#     new_l.append(i * i)
# print(new_l)

# 案例2
# new_l2 = []
# for i in l:
#     if i % 2 == 0:
#         new_l2.append(i)
# print(new_l2)


# 列表推导式： [表达式 for i in l if语句]
# l = [1, 2, 3, 4, 5]
# print([i for i in l])
# print([i * i for i in l])
# print([i for i in l if i % 2 == 0])

# 面试题：如何实现['1', '2', '3']变成[1, 2, 3]

# l = ["1", "2", "3"]

# print([int(i) for i in l])  # [1, 2, 3]

# 面试题：获取1-100中所有偶数平方列表
# print([i * i for i in range(1, 101) if i % 2 == 0])

# 双层循环
l = [[1, 2], [3, 4], [5, 6]]
# l = [1,2,3,4,5,6]

print([j for i in l for j in i if j % 2 == 0])
