# 案例1：
# d = {"a": 1, "b": 2}
# new_dict = {}
# for k, v in d.items():
#     new_dict[k.upper()] = v
#
# print(new_dict)

# 案例2：
# new_dict = {}
# for k, v in d.items():
#     new_dict[k] = v + 100
#
# print(new_dict)


# 字典推导式： {键表达式:值的表达式 for k,v in dict.items() if表达式}
d = {"a": 1, "b": 2}
print({k.upper(): v for k, v in d.items()})
print({k: v + 100 for k, v in d.items()})
# 键值对互换
print({v: k for k, v in d.items()})

# 面试题：统计一段字符串中每个字符出现的次数，比如`abcaabccab`
s = "abcaabccab"

# 方式1：
# d = {}
# for c in s:
#     d[c] = d.get(c, 0) + 1
# print(d)

# 方式2：
# print({char: s.count(char) for char in s if char != "b"})


# 1,2,3,4,5能组成多少个互不相同且无重复的三位数字？

l = [1, 2, 3, 4, 5]
new_l = []
for i in l:
    for j in l:
        for k in l:
            if i != j and i != k and j != k:
                v = int(str(i) + str(j) + str(k))
                new_l.append(v)

print(new_l)

ret = [int(str(i) + str(j) + str(k)) for i in l for j in l for k in l if i != j and i != k and j != k]
print(ret)


def f(x):
    print(id(x))
    # x.append(3)
    x = 10


x = [1, 2]
print(id(x))
f(x)
print(x)
