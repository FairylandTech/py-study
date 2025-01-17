my_dict = {'name': 'isaac'}
print(my_dict)
# 字典中添加和修改数据,使用key值进行添加和修改
# 字典[key] = 数据值;   如果key值存在,就是修改,如果key值不存在,就是添加

my_dict['age'] = 18  # key值不存在,添加
print(my_dict)

my_dict['age'] = 19  # key值已经存在,就是修改数据
print(my_dict)

# 注意点 key 值 int 的 1 和float的 1.0 代表一个key值
my_dict[1] = 'int'
print(my_dict)
my_dict[1.0] = 'float'
print(my_dict)

