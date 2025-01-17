n = int(input('请输入正方形的边长:'))
# n = 5

# 3. 打印 n 行的*
# 3.1 定义变量,记录打印了几行
j = 0
while j < n:
    # 2. 打印一行的*
    # 2.1 记录一行中已经打印的*个数
    i = 0
    while i < n:
        # 1. 打印一个*
        print('*', end=' ')   # 打印一行的时候, 不能换行
        i += 1
    # 一行打印结束之后,需要让j + 1, 同时还需要换行
    print()  # print函数默认会输出换行
    j += 1


# for 循环实现打印正方形
# 2. 打印n 行
for j in range(n):
    # 1. 打印一行
    for i in range(n):
        print('*', end=' ')
    print()  # 换行
