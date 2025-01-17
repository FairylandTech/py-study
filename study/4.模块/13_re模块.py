import re

# # 1.从一个字符串中提取到所有的数字
# lst = re.findall("\d+", "我今年18岁了. 我喜欢5个明细")
# print(lst)


# # 2. 判断一句话中是否有数字
# # search的特点: 匹配字符串, 匹配到第一个结果就返回. 不会匹配出多个结果来
# res =re.search('\d+', "我今年18岁了. 我喜欢5个明细")
# print(res.group())
# print(res.group())

# # finditer, 所有的数据都会进行匹配, 返回的是迭代器
# it = re.finditer("\d+", "我今年18岁了. 我喜欢5个明细")
# for item in it:
#     print(item.group())

# # match 匹配, 从头开始匹配   ^
# result = re.match("\d+", "18岁了. 我喜欢5个明细")
# print(result.group())


# result = re.split("[你的]", "你好18你岁的先生, 我特别你喜欢5米高的大楼")
# print(result)

# result  = re.sub("\d+", "_sb_", "admin18我的天18呵呵6的天下")
# print(result)

# result  = re.subn("\d+", "_sb_", "admin18我的天18呵呵6的天下")
# print(result)


# obj = re.compile("\d+")  # 先加载这个正则, 后面可以直接用这个正则去匹配内容
# # lst = obj.findall("我今天吃了3个馒头, 喝了2碗粥")
# # print(lst)
#
# lst = obj.finditer("我今天吃了3个馒头, 喝了2碗粥")
# for it in lst:
#     print(it.group())


# # 爬虫必会的一个重点
# # 1. ()括起来的内容是你最终想要的结果
# # 2. (?P<name>正则) 把正则匹配到的内容直接放在name组里面, 后面取数据的时候直接group(name)
#
# obj = re.compile(r"今天吃了(?P<mian>\d+)碗面, 又吃了(?P<xian>\d+)盘小咸菜")
# # 正则表达式中经常的出现\n, 为了避免这类问题出现. 可以在字符串前面写上r来直接把字符串中的内容全部当成普通字符来处理
# # print(r"你好我叫\n周杰伦")
# result = obj.finditer("明天我要吃4碗面,喝上8碗汤. 今天吃了5碗面, 又吃了6盘小咸菜, 昨天吃了1碗面条")
# for item in result:
#     # print(item.group("mian"))
#     # print(item.group("xian"))
#     print(item.groupdict())

# findall: 匹配所有, 返回列表
# finditer: 匹配所有, 返回迭代器
# search: 匹配到一个结果就返回
# match: 从头匹配, 得到一个结果就返回

# group: 拿到数据的.
# group(组名)

# re.compile() 预编译

# () 从正则匹配到的结果中拿到指定数据
# (?P<name>正则)
