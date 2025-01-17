my_str = 'hello python!'
# my_str = 'hello itcast!'

for i in my_str:
    if i == 'p':
        print('包含p这个字符')
        # 已经判断出来包含了,是否还需要继续判断
        break
else:
    print('不包含p这个字符')


