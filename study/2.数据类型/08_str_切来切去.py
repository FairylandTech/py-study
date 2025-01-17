# s = "sylar"
# s1 = s.center(10)
# print(s1)
#
# s2 = s.center(10, "*")
# print(s2)


# strip() 默认是去掉字符串左右两端的空白(空格, \t, \n)
# print("我爱呵\t你")  # 其实就是我们键盘上的tab键
# print("我也爱\n你啊")  # \n是换行

# s = " \t  \n    我今天心  情特别好      \t \n      "
# print(s.strip())  #

# username = input("请输入用户名:").strip()
# password = input("请输入密码:").strip()
# if username == 'admin' and password == '123':
#     print("登录成功!")
# else:
#     print("登录失败!")

# s = "sb_sylar_sb"
# print(s.strip("sb"))


# # replace()  字符串替换
# s = "我特别喜欢苍井空"
# s1 = s.replace("苍井空", "***")
# print(s1)

# # 请去掉一句话中所有的空格
# s = "  我    哎    你   哈哈   "
# s1 = s.replace(" ", "")  # 我哎你哈哈
# print(s1)

# # split() 字符串切割
# s = "张无忌_赵敏_周芷若_小昭_珠儿"
# lst = s.split("_")  # 通过_切割, 会得到很多个字符串
# print(lst)


# # join()  把一个列表组合成一个字符串
# lst = ['张无忌', '赵敏', '周芷若', '小昭', '珠儿']
# s = "_爱_".join(lst)
# print(s)  # 张无忌_爱_赵敏_爱_周芷若_爱_小昭_爱_珠儿

