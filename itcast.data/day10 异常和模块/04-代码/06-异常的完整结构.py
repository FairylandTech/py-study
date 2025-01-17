print('其他的代码......')
num = input('请输入一个数字:')
try:
    a = int(num)
    num = 10 / a
    print('计算得到的结果是:', num)
except Exception as e:
    print('你输入有误,请再次输入', e)
else:
    print('没有发生异常,我会会执行')
finally:
    print('不管有没有发生异常,我都会执行')

print('其他的代码......')