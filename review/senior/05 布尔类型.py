# print(2 > 1)

# 零值：每一个数据类型都有且只有一个布尔值为False的对象
# 整型的零值：0
# 字符串的零值：""
# 列表和字典零值：[] {}
# print(bool(0))
# print(bool(-1))
# print(bool(1))
# print(bool(-100))
#
# print(bool(""))
# print(bool("False"))
# print(bool("-1"))
# print(bool("0"))
#
# print(bool([]))
# print(bool([0, ]))
# print(bool({}))


# 短路计算:  与 and  或 or 非  not
# 真与真： 真
# 真与假： 假
# 假与真： 假
# 假与假： 假


# 真或真： 真
# 真或假： 真
# 假或真： 真
# 假或假： 假

# 非真即假
# 非假即真

# print(True and False)

print(1 and 2)
print(2 or 3)
print(0 or 3)


def login():
    user = None

    # if user:
    #     return user
    # else:
    #     return "匿名用户"

    return user or "匿名用户"


ret = login()
print(ret)

print(0 or 1 and 5)


