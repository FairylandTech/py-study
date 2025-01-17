# a 方式打开文件, 追加内容,在文件的末尾写入内容
# 文件不存在,会创建文件
# 注意点: 不管是a 方式打开文件,还是 w 方式打开文件,写内容,都是使用 write()函数
f = open('b.txt', 'a', encoding='utf-8')
# f.write('hello world!\n')
f.write('111\n')
f.close()
