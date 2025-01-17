# 异常: 程序运行过程中,代码遇到错误,给出错误的提示

print('其他的代码......')
num = input('请输入一个数字:')
# ZeroDivisionError: division by zero
# ValueError: invalid literal for int() with base 10: 'a'
num = 10 / int(num)
print('计算得到的结果是:', num)
print('其他的代码......')
