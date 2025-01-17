n = 5

# 2. 定义变量,记录打印的行数
j = 1  # 将要打印第一行
while j <= n:
    # 1. 定义变量记录一行打印的*个数
    i = 1  # 将要打印第一个
    while i <= j:
        print('*', end=' ')
        i += 1
    print()
    j += 1


# for循环打印三角形
for i in range(n):  # 控制行数
    for j in range(i+1):  # i  range(i) 不包含i  , 控制一行打印的个数
        print('*', end=' ')
    print()
