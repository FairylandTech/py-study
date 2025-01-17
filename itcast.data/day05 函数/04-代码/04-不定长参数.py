# print(1)
# print(1, 2)
# print(1, 2, 3)
# print(1, 2, 3, 4)
# print(1, 2, 3, 4, 5)


def func(args, kwargs):  # 两个普通的形参
    print(args)
    print(kwargs)


func(1, 2)
func(args=2, kwargs=1)

print('*' * 30)
print('*' * 30)


# 在形参前边加上一个*, 该形参变为不定长元组形参,可以接收所有的位置实参, 类型是元组
# 在形参前边加上两个**, 该形参变为不定长字典形参, 可以接收所有的关键字实参,类型是字典
def func(*args, **kwargs):
    print(args)
    print(kwargs)


func(1, 2, 3, 3, 4, 5)
func(a=1, b=2, c=3, d=4)
func(1, 2, 3, a=4, b=5, d=6)