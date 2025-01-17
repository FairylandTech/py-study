# 函数传参传递的也是引用
my_list = [1, 2, 3]  # 全局变量


def func1(a):
    a.append(4)


def func2():
    # 为啥不加global, 因为没有修改 my_list 中存的引用值
    my_list.append(5)


def func3():
    global my_list
    my_list = [1, 2, 3]   # 修改全局变量的值


def func4(a):
    # += 对于列表来说,类似列表的extend方法,不会改变变量的引用地址
    a += a  # a = a + a, 修改了a变量a的引用
    # print(a)


func1(my_list)    # [1, 2, 3, 4]
func2()  # [1, 2, 3, 4, 5]
func3()  # [1, 2, 3]
print(my_list)

b = 10  # 不可变类型
func4(b)
print(b)  #

func4(my_list)
print(my_list)  # [1, 2, 3, 1, 2, 3]
