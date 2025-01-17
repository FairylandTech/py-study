d = {"皮长山": "皮校长", "王长贵": "谢大脚", "谢广坤": '泻立停'}

# # 1.直接for循环, 直接拿到key, 记住
# for k in d:
#     print(k)
#     print(d[k])
#
# # 2. 借助字典的keys() 了解
# print(d.keys())
# for k in d.keys():
#     print(k)
#     print(d[k])

# # 3. 拿到所有的value
# for v in d.values():
#     print(v)

# # 4. 通过items()拿到所有数据, 最直接的拿到k和v的方案
# # print(d.items())
# for k, v in d.items():
#     print(k)
#     print(v)


# # 5. 解构
# a = 10, 20
# print(type(a))
#
# a, b = (10, 20)  # 解构
# print(a, b)


def add(n,i):
    return n+i


def test():
    for i in range(4):
        yield i


g = test()   # 生成器

n = 1
g1 = (add(n, i) for i in g)

n = 10
g2 = (add(n, i) for i in g1)

list(g2)


# for n in [1,10]:
#     g=(add(n,i) for i in g)
# print(list(g))
