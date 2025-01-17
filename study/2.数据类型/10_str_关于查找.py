# # 让用户输入一个名字, 判断这个名字是否以张开头
# # startswith()  判断字符串是否以xxx开头
# name = input("请输入你的名字:")
# if name.startswith("张"):
#     print("是的")
# else:
#     print("不是的")


# # endswith() 判断字符串是否以xxx结尾
# s = "今天天气不错"
# print(s.endswith("天气"))
# print(s.endswith("不错"))


# s = "python_java_php_ajax"
# print(s.count("#"))  # 计算字符串中出现了多少个xxx


# s = "我最喜欢python了"
# print(s.find("哈"))  # 查找字符串, 如果找到了就返回索引, 找不到-1
# print(s.find("python"))  # 4

# s = "我最喜欢python了"
# print(s.index("python"))  # 4  查找字符串, 返回索引
# print(s.index("#"))  # 找不到就报错
