# 1. 打开文件 w 方式打开文件,文件不存在,会创建文件, 文件存在,会覆盖清空原文件
f = open('a.txt', 'w', encoding='utf-8')
# 2. 写文件 文件对象.write(写入文件的内容)
f.write('hello world!\n')
f.write('hello python!\n')
f.write('你好,中国!')
# 3. 关闭文件
f.close()


