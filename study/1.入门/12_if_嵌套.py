# 模拟登录验证
username = input("请输入您的用户名: ")
password = input("请输入您的密码: ")

if username == 'admin':  # 假设正确的用户名是 admin
    # pass  # 保证代码语法结构的完整性
    # 进一步判断密码是否正确
    if password == "123456":
        print("登录成功!")
    else:
        print("对不起, 密码错误. ")

else:
    print("对不起, 您输入的用户名不正确. ")


