my_dict = {'name': 'isaac', 'age': 19, 1: 'float', 2: 'aa'}

# 根据key值删除数据  del 字典名[key]
del my_dict[1]
print(my_dict)

# 字典.pop(key)  根据key值删除, 返回值是删除的key对应的value值
result = my_dict.pop('age')
print(my_dict)
print(result)

# 字典.clear()  清空字典, 删除所有的键值对
my_dict.clear()
print(my_dict)


# del 字典名   直接将这个字典删除了,不能使用这个字典了
del my_dict  # 后边的代码不能再直接使用这个变量了,除非再次定义

# print(my_dict)  代码报错, 变量为定义


