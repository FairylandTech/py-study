# 组包, 将多个数据值,组成元组,给到一个变量.
a = 1, 2, 3
print(a)  # (1, 2, 3)


def func():
    return 1, 2  # 组包


# 拆包: 将容器的数据分别给到多个变量, 需要注意: 数据的个数和变量的个数要保持一致
b, c, d = a   # 拆包
# print(b, c, d)

e, f = func()
print(e, f)

my_list = [10, 20]
a, b = my_list
print(a, b)
my_dict = {'name': 'isaac', 'age': 18}
a, b = my_dict   # key值
print(a, b)

