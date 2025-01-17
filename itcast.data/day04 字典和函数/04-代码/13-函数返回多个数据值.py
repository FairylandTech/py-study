def func(a, b):
    c = a + b
    d = a - b
    # 需求: 想要将 c 和 d 都进行返回
    # 思考: 容器可以保存多个数据值, 那就可以将 c  和 d 放到容器中进行返回
    # return [c, d]
    # return (c, d)
    # return {'c': c, 'd': d}
    # return {0: c, 1: d}
    return c, d  # 默认是组成元组进行返回的


result = func(10, 20)
print(f"a+b的结果是{result[0]}, a-b的结果是{result[1]}")

