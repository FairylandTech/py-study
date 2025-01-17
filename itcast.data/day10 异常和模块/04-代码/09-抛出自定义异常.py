# 1. 定义异常类, 密码长度不足的异常
class PasswordLengthError(Exception):
    # def __str__(self):
    #     return 'xxxxxx'
    pass


def get_password():  # 等同于系统定义函数
    password = input('请输入密码:')
    if len(password) >= 8:
        print('密码长度合格')
    else:
        # 抛出异常
        raise PasswordLengthError('密码长度不足8位')
        # print('密码长度不足8位')

try:
    get_password()  # 调用系统的函数
except PasswordLengthError as e:
    print(e)

print('其他代码.....')

