# def chi(main_food, fu_food, soup, sweet):
#     print(main_food, fu_food, soup, sweet)
#
#
# chi("大米饭", "土豆炖豆角", "紫菜蛋花汤", "哈根达斯")
# chi("大米饭")
# chi("大米饭", "面条", "土豆", "胡辣汤", "蒙牛youyisi", "哈根达斯", "伊利")


# # 动态传参: 给出多个参数, 在形参位置, 一次性接收
# # * :动态接收位置参数, 自动打包成元组
# def chi(*food):  # 可以接受任意个位置参数
#     print(food)
#
# chi("大米饭")
# chi("大米饭", "面条")
# chi("胡辣汤", "哈根达斯", "炖牛肉")

# # **: 动态接收关键字参数, 接收到的参数是字典
# def chi(**food):  # 接收关键字参数
#     print(food)
#
# chi(main_food="面条", fu_food="土豆炖牛肉")


# 实参:
#   1. 位置参数
#   2. 关键字参数
#   3. 混合参数, 先位置, 后关键字

# 形参:
#     1. 位置参数
#     2. 默认值参数
#     3. 动态传参
#       混合着使用, 一定要注意, 代码的顺序
#       正确的顺序: 位置参数 > *args > 默认值参数 > **kwargs
#       上面的参数可以任意的搭配使用, 但是顺序不能变

# def func(a, *args, c="呵呵", **kwargs):
#     print(a, args, c)
#
# func("嘚吧嘚")  # c使用了默认值, args就没有数据
# func("你好", "不好")  # c使用了默认值, args就没有数据
# func("你好", "不好", "哈哈", "真棒", hehe="哈哈", a="么么", c="哒哒")  # args如果有数据. 默认值就没用了

# def func(a, *args):
#     print(args)


# def func(*args, **kwargs):  # 该函数可以接受任意的参数
#     print(args)
#     print(kwargs)
#
# func("你好", "你不好", a="你很好", b="真好")


# # 一定要合理的使用参数
# def func(a, b, c):
#     pass


print("你好", "你不好", "你很好", "嘚吧嘚", "大鹏", "于莎莎", sep="_", end="sb")
print("哒哒哒哒哒哒哒哒哒冒蓝火的加特林")
# def print(*args, sep=' ', end='\n'):
