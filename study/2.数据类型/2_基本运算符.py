# a = 10
# b = 20
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
#
# print(a // b)  # 计算商
# print(a % b)   # 计算余数
#
# print(3 ** 4)  # 次幂计算


# 比较运算
# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)


# a = 10
# b = 20

# # a = b  # 计算. 把b的值赋值给a
# a += b  # 累加计算  相当于a = a + b
# a -= b
# a *= b
# a /= b
# a %= b
# print(a)
# print(b)
#
# i = 1
# while i <= 100:
#     print(i)
#     # i = i + 1
#     i += 1  # 循环尽量这么写


# 逻辑运算 -> 布尔值
# and   并且. and左右两端同时为真. 结果才能是真. 有一个是假, 结局就是假
# or    或者. or左右两端, 有一个是真的, 那么结果就是真的.
# not   非,不.  非真既假, 非假既真

# print(True and False)
# print(True or False)
# print(not False)

# 重点, 当出现and, or, not, () 混合使用的时候.
#   运算顺序
#      ()  ->  not  ->  and   ->  or

# 练习
# print(True or (False and True) or not False and True)
# print(1 > 2 or 3 < 4 and 4 > 6)
#       F or T and F
#           F


# 非常规情况
# 当出现数字进行逻辑计算怎么办
# 非零当成True
# 零当成False
# 记住or就可以了. and和or正好相反
# print(1 or 0)
# 根据True or False能够得出结论. 最后的结果应该跟着前面那个数来得到
# 所以, 结果跟着前面的那个数走. 结果就是1


# print(0 or 3)  # 3
# print(1 or 3)   # 1

# print(1 and 0)

# or
# # x or y
# if x == 0:
#     结果就是y
# else:
#     结果就是x

# and和or相反
# # x and y
# if x == 0:
#     结果就是x
# else:
#     结果就是y

#            4           0         0
# print(0 or 3 and 4 or 0 and 5 or 1 and 0)


# 真是开发中如何使用and 和 or
# 登录
# username = input("请输入用户名:")
# password = input("请输入密码:")
# if username == 'admin' and password == "123456":
#     print("登录成功")
# else:
#     print("登录失败")

# 盖伦:
# Q or 鼠标点击技能:
#      第一个技能


# # 成员运算
# # in ,  not in
# # 让用户输入评论信息. 需要过滤敏感词.
# # 判断敏感词
# content = input("请输入评论: ")
# if "苍井空" in content:
#     print("有敏感词")
# else:
#     print("没有敏感词")

# # 升级需求:
# # 判断苍井空 或者 小泽玛利亚是否出现在评论里
# content = input("请输入评论: ")
# if "苍井空" in content or "小泽玛利亚" in content:
#     print("有敏感词")
# else:
#     print("没有敏感词")
