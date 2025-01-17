l = [1, 2, 3, 4, 5]

# print([i for i in l if i % 2 == 0])

ret = filter(lambda item: item % 2 == 0, l)
print(list(ret))

# 有个列表a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8] 使用filter 函数过滤出大于0的数
a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
print(list(filter(lambda item: item > 0, a)))

b = [
    {"name": "张三", "score": 66},
    {"name": "李四", "score": 88},
    {"name": "王五", "score": 90},
    {"name": "陈六", "score": 56},
]
print(list(filter(lambda item: item["score"] > 60, b)))

# map 请将列表 [1,2,3,4,5] 使用map函数转变成 [1,4,9,16,25]
c = [1, 2, 3, 4, 5]
print(list(map(lambda item: item ** 2, c)))


# map函数对列表a=[1,3,5],b=[2,4,6]相乘得到[2,12,30]
a = [1, 3, 5]
b = [2, 4, 6]
print(list(map(lambda x, y: x * y, a, b)))

# 将 'python is shell' 转为 'nohtyp si llehs'
s= 'python is shell'

l = s.split(" ")
print(" ".join(list(map(lambda item:item[::-1],l))))


