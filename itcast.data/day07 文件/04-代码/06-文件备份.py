# 1. 用只读的方式,打开文件
f = open('a.txt', 'rb')
# 2. 读取文件内容
buf = f.read()
# 3. 关闭文件
f.close()
# 4. 只写的方式,打开新文件
f_w = open('a[备份].txt', 'wb')
# 5. 将 第 2 步读取的内容写入新文件
f_w.write(buf)
# 6. 关闭新文件
f_w.close()