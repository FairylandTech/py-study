# 异常: 程序代码在运行过程中遇到的错误, 程序会报错,会终止程序代码的运行.
# 异常捕获: 是指在程序代码运行过程中,遇到错误, 不让程序代码终止,让其继续运行, 同时可以给使用者一个提示信息
# 并记录这个错误, 便于后期改进
"""
try:
    可能发生异常的代码
except 异常的类型:
    发生异常执行的代码
"""


print('其他的代码......')
num = input('请输入一个数字:')
# ZeroDivisionError: division by zero
# ValueError: invalid literal for int() with base 10: 'a'
try:
    num = 10 / int(num)
    print('计算得到的结果是:', num)
except ZeroDivisionError:
    print('你输入有误,请再次输入')

print('其他的代码......')