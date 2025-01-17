# f被称为文件句柄, 负责操纵你打开的这个文件
#          路径
#           绝对路径, 相对路径(用的多)

f = open("../a/b/32_a_txt.txt", mode="r", encoding="utf-8")
print(f.read())  # 读取全部内容



