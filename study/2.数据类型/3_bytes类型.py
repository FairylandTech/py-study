# s = "中国"  # 内存中使用的是unicode
#
# # 编码
# bs = s.encode("utf-8")
# print(bs)  # b'\xe4\xb8\xad\xe5\x9b\xbd'
# # bytes
# bs = b'\xe4\xb8\xad\xe5\x9b\xbd'  # 每个\x一个字节
# print(type(bs))
#
#
# s = "中国"
# print(s.encode('gbk'))  # b'\xd6\xd0\xb9\xfa'

# # 把bytes转化回字符串
# # decode() 解码
# bs = b'\xd6\xd0\xb9\xfa'
# s = bs.decode("gbk")
# print(s)

# 不同的编码之间是不能直接进行转换的
bs = b'\xd6\xd0\xb9\xfa'
# 转化成utf-8的字节
s = bs.decode("gbk")
print(s.encode("utf-8"))  # b'\xe4\xb8\xad\xe5\x9b\xbd'


# encode()
# decode()
# bytes : python程序中最小的数据单位
#  byte -> 8个01
# 你好, 我叫周杰伦
# 图片, mp3, 视频 => bytes
# 3kb
# apples
