# 1. 打开文件
f = open('a.txt', 'r', encoding='utf-8')
# 2. 读写文件 文件对象.read(n)  n 一次读取多少字节的内容,默认不写,读取全部内容
buf = f.read(3)
print(buf)  # 123
print('-'*30)
buf = f.read(3)  #
print(buf)
# 3. 关闭文件
f.close()


