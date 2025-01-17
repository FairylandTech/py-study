f = open('c.txt', 'wb')
f.write('你好'.encode())   # encode() 将str 转换为二进制格式的字符串
f.close()


f1 = open('c.txt', 'rb')
buf = f1.read()
print(buf)
print(buf.decode())
f1.close()