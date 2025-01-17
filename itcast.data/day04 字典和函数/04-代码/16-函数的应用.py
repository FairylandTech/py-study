# 1. 定义一个函数,打印一条横线
def print_line():
    print('-' * 30)


# 2. 定义一个函数,打印任意条数的横线
def print_lines(n):
    for i in range(n):
        print_line()


# print_line()
# print_lines(4)
print_lines(5)
