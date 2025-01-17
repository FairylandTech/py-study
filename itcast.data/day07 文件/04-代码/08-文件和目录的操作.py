# 对文件和目录的操作,需要导入 os 模块
import os

# 1. 文件重命名 os.rename(原文件路径名, 新文件路径名)
# os.rename('a.txt', 'aa.txt')
# 2. 删除文件 os.remove(文件的路径名)
# os.remove('aa.txt')
# 3. 创建目录 os.mkdir(目录路径名)  make directory
# os.mkdir('test')
# os.mkdir('test/aa')

# 4. 删除空目录  os.rmdir(目录名)  remove directory
# os.rmdir('test/aa')
# 5. 获取当前所在的目录 os.getcwd()  get current working directory
buf = os.getcwd()
print(buf)
# 6. 修改当前的目录 os.chdir(目录名)  change dir
os.chdir('test')
buf = os.getcwd()
print(buf)
# 7. 获取指定目录中的内容,  os.listdir(目录), 默认不写参数,是获取当前目录中的内容
# 返回值是列表, 列表中的每一项是文件名
buf = os.listdir()   # test
print(buf)

