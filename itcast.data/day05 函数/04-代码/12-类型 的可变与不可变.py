# 类型的可变与不可变: 在不改变变量引用的前提下,能否改变变量中引用中的数据,
# 如果能改变是可变类型, 如果不能改变,是不可变类型
# int float bool str list tuple dict
# 不可变类型:  int float bool str  tuple
# 可变类型: list dict

# num = 10
# num = 20
#
# my_list = [1, 2]
# my_list.append(3)

a = 1000
b = 1000
print(id(a), id(b))  # python中的内存优化,对于不可变类型进行的,
print(id(a) == id(b))

a = 'hello'
b = 'hello'
print(id(a), id(b))  # python中的内存优化,对于不可变类型进行的,

my_tuple = (1, 2)
my_tuple1 = (1, 2)
print(id(my_tuple), id(my_tuple1))
print(id(my_tuple) == id(my_tuple1))
print('-' * 20)
my_list = [1, 2, 3]
my_list1 = [1, 2, 3]
print(id(my_list), id(my_list1))

print('*' * 30)
my_tuple2 = (1, 2, [3, 4])
print(my_tuple2)
my_tuple2[2][1] = 10
print(my_tuple2)
