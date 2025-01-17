# 1. 打开文件, 是文件从硬盘中存到内存中
# open(file, mode='r',  encoding)
# file 要操作的文件名字, 类型是 str
# mode, 文件打开的方式, r(read) 只读打开, w(write) 只写打开  a(append) 追加打开
# encoding  文件的编码格式, 常见的编码格式有两种, 一种是gbk, 一种是utf-8
# 返回值, 文件对象, 后续所有的文件操作,都需要通过这个文件对象进行

# 以只读的方式打开当前目录中,1.txt 文件, 文件不存在会报错
f = open('1.txt', 'r')
# 2. 读文件 文件对象.read()
buf = f.read()
print(buf)
# 3. 关闭文件  文件.close()  将内存中三大文件同步到硬盘中
f.close()



