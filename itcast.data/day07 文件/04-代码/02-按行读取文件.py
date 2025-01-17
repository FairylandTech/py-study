f = open('a.txt', 'r', encoding='utf-8')
# f.readline()  # 一次读取一行的内容, 返回值是读取到的内容(str)
# buf = f.readline()

# f.readlines()  # 按行读取,一次读取所有行,返回值是列表, 列表中的每一项是一个字符串,即一行的内容
buf = f.readlines()
print(buf)
buf = [i.strip() for i in buf]
print(buf)
f.close()
