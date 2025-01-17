f = open('a.txt', 'r', encoding='utf-8')
while True:
    buf = f.readline()
    if buf:  # if len(buf) > 0   容器,可以直接作为判断条件,容器中有内容,为True,没有数据是False
        print(buf, end='')
    else:
        # 文件读完了
        break

f.close()


