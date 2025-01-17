def func(n):
    num = 1
    for i in range(1, n + 1):
        num = num * i

    print(num)


def func2(n):
    if n == 1:
        return 1
    # 想要求 n! , 只需要(n-1)! * n
    num = func2(n-1) * n
    return num


# func(5)
print(func2(5))
