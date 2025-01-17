num = 10  # num中存储了数据10
print('50%')
print('%d%%' % 50)

# for i in range(1, 10, 2):
#     print(i)
#
#
# for i in range(10, 1, -2):
#     print(i)


def show():
    global num
    num = 20
    print(num)


show()
print(num)

