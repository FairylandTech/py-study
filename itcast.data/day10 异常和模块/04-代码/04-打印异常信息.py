"""
try:
    可能发生异常的代码
except (异常的类型1, 异常类型2, ...) as 变量名:
    发生异常执行的代码
    print(变量名)
"""


print('其他的代码......')
num = input('请输入一个数字:')
# ZeroDivisionError: division by zero
# ValueError: invalid literal for int() with base 10: 'a'
try:
    a = int(num)
    num = 10 / a
    print('计算得到的结果是:', num)
except (ZeroDivisionError, ValueError) as e:
    print('你输入有误,请再次输入', e)

print('其他的代码......')