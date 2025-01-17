print('其他的代码......')
num = input('请输入一个数字:')
try:
    a = int(num)
    num = 10 / a
    print('计算得到的结果是:', num)
    f = open('1.txt', 'r')
except Exception as e:
    print('你输入有误,请再次输入', e)

print('其他的代码......')