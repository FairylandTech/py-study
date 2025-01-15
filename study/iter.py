# coding=UTF-8

# 迭代器, 可以被循环的(for)的数据类型, 该数据类型在内部实现了__iter__()的方法
# 列表, 元组, 字典, 字符串

# print(list(range(10)))  # range() 会生成一个可迭代对象

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list.__iter__()  # Cpython 已经帮你实现好了

# for i in data:
#     print(i)

# for i in data.__iter__():
#     print(i)

# iter_data = data.__iter__()
iter_data = iter(data)

print(iter_data.__next__())
print(iter_data.__next__())
print(iter_data.__next__())
print(iter_data.__next__())
print(iter_data.__next__())
print(iter_data.__next__())
print(iter_data.__next__())
print(iter_data.__next__())
print(iter_data.__next__())
print(iter_data.__next__())
# print(iter_data.__next__())

letters = "abcdefghij"

for letter in letters:
    print(letter)

for letter in letters.__iter__():
    print(letter)
