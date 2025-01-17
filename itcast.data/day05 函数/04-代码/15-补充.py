def func(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)
    num = 0
    # for i in args:
    #     num += i  # num = num + i
    #
    # for j in kwargs.values():
    #     num += j
    #
    # print(f"求和的结果为{num}")


my_list = [1, 2, 3, 4, 5, 6]
my_dict = {'a': 7, 'c': 8, 'b': 9, 'd': 10}

# func(my_list)  # 将列表作为一个数据进行传递
# func(*my_list)  # 将列表中的每一个数据作为位置参数进行传递, 拆包

# func(my_dict)  # 将my_dict 作为一个位置实参进行传递
# func(*my_dict)  # 将my_dict中的key 作为位置实参进行传递
func(**my_dict)  # 将my_dict中键值对作为关键字实参进行传递
