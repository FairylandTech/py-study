# 一 列表

# 增删改查

# 添加 append  insert  extend

l = [1, 2, 3]
l.append(4)
print(l)  # [1, 2, 3, 4]

l.insert(0, 100)
print(l)

l.append([5, 6, 7])
print(l)
l.extend([8, 9])
print(l)

print([1, 2] + [3, 4])

# 删除： pop  remove  clear

print(l)
l.pop(0)
print(l)
l.remove(8)
print(l)
# l.clear()
# print(l)

# 其它 sort

l2 = [2, 4, 1, 3, 9, 5, 6]
l2.sort(reverse=True)
print(l2)  # [1, 2, 3, 4, 5, 6, 9]

l3 = ["Alex", "Eric", "Babana", "Alvin"]
# l3.sort()
# print(l3)
# print(l3.index("Alex"))
l3.reverse()
print(l3)

l3.count("Alex")  # 1
print(len(l3))

# 二 元组： 只读列表

t = (1, 2, 3, 1)
print(t.count(1))
print(t.index(3))

# 三 集合：去重
s = {1, 2, 3, 1}
print(s)

# l = [1, 2, 3, 2, 3]
# print(list(set(l)))


# 面试题

# (1)将两个列表[1, 5, 7, 9],[2, 2, 6, 8]合并为[1, 2, 2, 5, 6, 7, 8, 9]
l1 = [1, 5, 7, 9]
l2 = [2, 2, 6, 8]
# print(l1 + l2)
l1.extend(l2)
print(l1)

# (2) a = [1,2,3,4,5,6]，a[::-3] 的结果是
a = [1, 2, 3, 4, 5, 6]
print(a[::-3])  # [6,3]

# (3) 列表去重再排序
l3 = [5, 8, 2, 4, 9, 1, 0, 6, 1, 5]
l4 = list(set(l3))
l4.reverse()
print(l4)

# (4) s = 'ajldjlajfdljfddd'，去重并从小到大排序输出'adfjl'

s = 'ajldjlajfdljfddd'
print(set(s))
l5 = list(set(s))
l5.sort()
print("".join(l5))
