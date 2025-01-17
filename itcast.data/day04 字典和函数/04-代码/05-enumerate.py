my_list = ['a', 'b', 'c', 'd', 'e']

# for i in my_list:
#     print(i)

for i in my_list:
    print(my_list.index(i), i)  # 下标, 数据值


# enemerate 将可迭代序列中元素所在的下标和具体元素数据组合在一块,变成元组
for j in enumerate(my_list):
    print(j)
