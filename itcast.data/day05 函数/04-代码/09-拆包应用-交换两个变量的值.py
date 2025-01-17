a = 10
b = 20

# 方法一:
# c = a
# a = b
# b = c
# print(a, b)

# 方法二: +/-   */÷
# a = a + b  # a 30
# b = a - b  # 10
# a = a - b  # 20
# print(a, b)

# 方法三, python中的使用 组包和拆包
a, b = b, a
print(a, b)
