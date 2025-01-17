def my_sum(*args, **kwargs):
    num = 0
    for i in args:
        num += i  # num = num + i

    for j in kwargs.values():
        num += j

    print(f"求和的结果为{num}")


my_sum(1, 2, 3, a=4, b=5, c=6)

