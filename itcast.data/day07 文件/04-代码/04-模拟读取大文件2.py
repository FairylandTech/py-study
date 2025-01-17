f = open('b.txt', 'r', encoding='utf-8')
while True:
    buf = f.read(5)  # f.read(4096)
    if buf:
        # print(buf, end='')
        print(buf)
    else:
        break

f.close()
