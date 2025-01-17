def my_sum(a, b, c):
    return a + b + c


def average(a, b, c):
    res = my_sum(a, b, c)
    return res / 3  # / 除法运算得到的数据是float类型


result = my_sum(1, 2, 3)
print(result)   # 6

result = average(1, 2, 3)
print(result)  # 2.0
