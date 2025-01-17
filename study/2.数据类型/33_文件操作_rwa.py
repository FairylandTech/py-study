# # r:  read 只读模式.
# f = open("a.txt", mode="r", encoding='utf-8')
# 1.read() 直接全部读取出来. 内存容易炸
# print(f.read())
# 2.readline()  一次读取一行
# print(f.readline())
# print(f.readline())
# # 3.for循环(重点)
# for line in f:  # 每次循环读取一行内容
#     print(line.strip())  # 去掉换行
# # 4.前面一行单独读取, 后面数据用for循环
# first = f.readline()
# print(first)
# print("===========")
# for line in f:
#     print(line)

# # w: write 只写模式, 重新创建文件
# f = open("b.txt", mode="w", encoding="utf-8")
# f.write("周杰伦")
# f.write("\n")  # 换行
# f.write("哈哈")

# # a: append 追加写. 不会重新创建文件, 但是如果文件不存在, 可以创建文件
# f = open("c.txt", mode="a", encoding="utf-8")
# f.write("你好")

# # b: bytes, 二进制  一般处理非文本文件, 不能指定encoding
# # rb 读取字节
# # wb 写入字节
# f1 = open("a/tu.jpg", mode="rb")
# f2 = open("c/tu.jpg", mode="wb")
# for line in f1:
#     f2.write(line)

# # +: 扩展  r+ w+ a+, r+b w+b a+b
# f = open("d.txt", mode="r+", encoding='utf-8')
# print(f.read())
# f.write("后天天气不好")
# f.close()

# 另类的一种写法, 可以省略掉close
# f1 = open()
with open("d.txt", mode="r", encoding="utf-8") as f1, \
     open("e.txt", mode="w", encoding='utf-8') as f2:
    for line in f1:
        f2.write(line)
    # f1.close()







