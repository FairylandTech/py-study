# a = 0
#
# b = bool(a)
# print(b)
# # 数字, 零当成False来用, 非零当成True来用
# while 1:  # 1比True好. 好在少些几个字母
#     print("爱你")

# a = ""  # 对于字符串, 只有空字符串是False, 其他都是True
# print(bool(a))

# a = []
# print(bool(a))

# 结论1: 所有的空的东西都可以表示False

# # 把字符串转化成数字  int()
# a = "123"
# print(type(int(a)))

# # 把数字, 变成字符串
# a = 1
# b = str(a)
# print(type(b))

# 结论2: 对于: int, str, bool而言.想互相的转化的时候,
# 想转化成谁. 就用谁把数据括起来
# int()
# str()
# bool()

# a = True
# print(int(a))
