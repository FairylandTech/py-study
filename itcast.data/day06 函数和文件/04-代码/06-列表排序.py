# 列表排序, 列表中的数据的类型要保持一致
my_list = [1, 3, 5, 4, 2, 1]
my_list.sort()
print(my_list)

list1 = [{'name': 'd', 'age': 19},
         {'name': 'b', 'age': 16},
         {'name': 'a', 'age': 16},
         {'name': 'c', 'age': 20}]

# list1.sort()  # 程序报错
# 匿名函数的形参是列表中的每一个数据
list1.sort(key=lambda x: x['name'])
print(list1)
list1.sort(key=lambda x: x['age'])
print(list1)

list2 = ['aghdd', 'bc', 'ghlj', 'def', 'ab']
list2.sort()
# print(list2)
# 需求: 根据列表中字符串的长度,列表进行排序
# list2.sort(key=len)
list2.sort(key=lambda x: len(x))
print(list2)

# sort(key= lambda 形参: (排序规则1, 排序规则2, ...))
# 当第一个规则相同,会按照第二个规则排序

# list1.sort(key=lambda x: (x['age'], x['name']))
# list1.sort(key=lambda x: (x['age'], x['name']), reverse=True)
# print(list1)

