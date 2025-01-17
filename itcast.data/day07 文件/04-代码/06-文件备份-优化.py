file_name = input('请输入要备份的文件名')

# 1. 用只读的方式,打开文件
f = open(file_name, 'rb')
# 2. 读取文件内容
buf = f.read()
# 3. 关闭文件
f.close()

# 根据原文件名,找到文件后缀和文件名
index = file_name.rfind('.')
# 后缀  file_name[index: ]
# 新文件名
new_file_name = file_name[:index] + '[备份]' + file_name[index:]
print(new_file_name)
# 4. 只写的方式,打开新文件
f_w = open(new_file_name, 'wb')
# 5. 将 第 2 步读取的内容写入新文件
f_w.write(buf)
# 6. 关闭新文件
f_w.close()

