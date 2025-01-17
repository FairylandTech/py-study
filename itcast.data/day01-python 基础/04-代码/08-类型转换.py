# # 1. 使用input函数获取苹果的价格
# price = input('请输入苹果价格:')  # str
# # 2. 使用input函数获取购买的重量
# weight = input('请输入重量:')  # str
# # 3. 输出想要的结果
# result = float(price) * float(weight)  # 类型转换
# print(f'苹果单价为{price}元/斤,购买了{weight}斤, 需要支付{result}元')

# 类型转换,将原始数据转换为我们需要的数据类型,在这个过程中,不会改变原始的数据,会生成一个新的数据
# 1. 转换为int类型  int(原始数据)
# 1.1 float类型的数据 转换为int
pi = 3.14
num = int(3.14)
# print(type(pi))   # float
# print(type(num))  # int

# 1.2 整数类型的字符串, "10"
my_str = '10'
num1 = int(my_str)
# print(type(my_str))  # str
# print(type(num1))  # int

# 2. 转换为 float类型 float()
# 2.1 int ---> float
num2 = 10
num3 = float(num2)
# print(type(num2))  # int
# print(type(num3))  # float

# 2.2 将数字类型字符串转换为 float  "10"  "3.14"
num4 = float("3.14")
num5 = float("10")
# print(type(num4))  # float
# print(type(num5))  # float

# eval()  还原原来的数据类型,  去掉字符串的引号
num6 = eval('100')  # 100 int
num7 = eval('3.14')  # 3.14 float
print(type(num6))
print(type(num7))

num8 = eval('num7')  # num7  是已经定义好的变量,可以使用,不会报错
print(num8, type(num8))
# num8 = eval('hello')   # 代码报错,hello 变量没有定义,不能使用




