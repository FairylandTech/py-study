# 变量的数据类型,由变量中存储的数据决定的
# 可以使用 type() 函数得到变量的数据类型, 想要进行输出,需要使用print函数

# int  整数
result = 10
# 1. 先使用 type() 函数获得变量result的数据类型 , 2, 使用print函数输出这个数据类型
print(type(result))  # <class 'int'>

# float 小数
result = 3.14  # 修改变量中存储的数据
print(type(result))   # <class 'float'>

# str 引号引起来的内容就是字符串, 包含单引号和双引号
name = 'isaac'
print(type(name))   # <class 'str'>
name = "hello"
print(type(name))

# bool 布尔类型, 只有两个值 True, False
result = True
print(type(result))   # <class 'bool'>

