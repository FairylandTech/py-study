# 列表推导式, 为了快速的生成一个列表
# 1. 变量 = [生成数据的规则 for 临时变量 in xxx]
# 每循环一次,就会创建一个数据
my_list = [i for i in range(5)]
print(my_list)  # [0, 1, 2, 3, 4]

my_list1 = ['hello' for i in range(5)]
print(my_list1)

my_list2 = [f'num:{i}' for i in my_list]
print(my_list2)
my_list3 = [i+i for i in range(5)]
print(my_list3)

# 2. 变量 = [生成数据的规则 for 临时变量 in xxx if xxx]
# 每循环一次,并且if条件为True,生成一个数据
my_list = [i for i in range(5) if i % 2 == 0]
print(my_list)  # [0, 2, 4]

# 3. 变量 = [生成数据的规则 for 临时变量 in xxx  for j in xxx]
# 第二个for 循环 循环一次,生成一个数据
my_list4 = [(i,j) for i in range(3) for j in range(3)]
print(my_list4)


# 补充: 字典推导式 
# 变量 = {生成字典的规则 for 临时变量 in xx}
# my_dict = {key: value for i in range(3)}
my_dict = {f"name{i}": i for i in range(3)}
print(my_dict)

my_dict = {f"name{i}": j for i in range(3) for j in range(3)}
print(my_dict)  # 3
my_dict = {f"name{i}{j}": j for i in range(3) for j in range(3)}
print(my_dict)

