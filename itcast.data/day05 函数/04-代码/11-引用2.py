my_list = [1, 2, 3]  # 将列表的引用地址保存到变量my_list 中
my_list1 = my_list  # 将my_list 变量中存储的引用地址给到 my_list1
print(my_list, id(my_list))
print(my_list1, id(my_list1))

my_list.append(4)  # 向列表中添加数据4, 将数据4 的引用保存到列表中
print(my_list, id(my_list))
print(my_list1, id(my_list1))

my_list[2] = 5
print(my_list, id(my_list))
print(my_list1, id(my_list1))
