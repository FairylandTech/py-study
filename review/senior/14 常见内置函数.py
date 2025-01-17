# zip函数

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(zip(l1,l2)))

# 面试题1 如何把元组("a","b")和元组(1,2)，变为字典{"a":1,"b":2}

# key = ("a", "b")
# value = (1, 2)
# print(dict(list(zip(key, value))))


# 面试题2 一条语句把 L=[(1,2), (3,4)] 转换成 [(1,3),(2,4)]，可以写下不同的方法
# L=[(1,2), (3,4)]

# print(list(zip(L[0],L[1]))) # [(1, 3), (2, 4)]


# sorted函数

l = (3, 1, 4, 6, 2)
# l.sort()
# print(l)

print(sorted(l))

# 自定义排序规则

# 案例1
l = [("yuan", 22), ("rain", 18), ("alvin", 32)]


def foo(item):
    return item[1]


print(sorted(l, key=foo))

print(sorted(l, key=lambda item: item[1]))

# 案例2

l2 = [{"name": "yuan", "score": [100, 90, 100]}, {"name": "rain", "score": [90, 78, 98]},
      {"name": "alvin", "score": [34, 56, 99]}]


def bar(item):
    return item["score"][2]


print(sorted(l2, key=lambda i: i["score"][2], reverse=True))

# foo = lambda x, y: x + y
# print(foo(2, 3))
# print((lambda x, y: x + y)(3, 4))



