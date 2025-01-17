"""
try:
    可能发生异常的代码
except (异常的类型1, 异常类型2, ...):
    发生异常执行的代码
"""


# print('其他的代码......')
# num = input('请输入一个数字:')
# # ZeroDivisionError: division by zero
# # ValueError: invalid literal for int() with base 10: 'a'
# try:
#     a = int(num)
#     num = 10 / a
#     print('计算得到的结果是:', num)
# except (ZeroDivisionError, ValueError):
#     print('你输入有误,请再次输入')
#
# print('其他的代码......')

"""
try:
    可能发生异常的代码
except 异常类型1:
    发生异常1,执行的代码
except 异常类型2:
    发生异常2,执行的代码
except ...:
    pass
"""
print('其他的代码......')
num = input('请输入一个数字:')
# ZeroDivisionError: division by zero
# ValueError: invalid literal for int() with base 10: 'a'
try:
    a = int(num)
    num = 10 / a
    print('计算得到的结果是:', num)
except ZeroDivisionError:
    print('你输入有误,请再次输入')
except ValueError:
    print('输入有误,请输入数字')

print('其他的代码......')
