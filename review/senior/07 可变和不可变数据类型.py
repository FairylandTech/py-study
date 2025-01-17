# 不可变数据类型：整型、字符串、布尔类型、元组
# x = 10
# x = 20
# print(x)
#
# s = "hello"
# s = s.upper()
# print(s)

# 可变数据类型：列表和字典

# l = [1, 2, 3]
# l[0] = 100
# print(l)


# 关于内置方法

# l.append(4)
# print(l)

# l.sort()
# print(l)

# 案例1
l1 = [1, 2, 3]
l2 = [4, 5, l1]
# l1[0] = 100
# print(l2)
l1 = [100, 2, 3]
print(l2)

# 案例2:

l1 = [1, 2, 3]
d = {"a": l1}
# l1.append(4)
l1 = [2, 3, 4]
print(d)
