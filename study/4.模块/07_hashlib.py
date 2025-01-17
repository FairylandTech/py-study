import hashlib

# # 创建md5对象
# obj = hashlib.md5()
# # 把要加密的信息传递给obj
# obj.update("666666".encode("utf-8"))
# # 从obj中拿到密文
# mi = obj.hexdigest()
# print(mi)  # f379eaf3c831b04de153469d1bec345e


# # 正常的默认加密过程是容易撞库的
# # 解决撞库: 加盐
# obj = hashlib.md5(b'flkjadsklfjaskjfladsjl')
# obj.update("666666".encode("utf-8"))
# print(obj.hexdigest())   # a4dd002a8650f53dd5c655d5cb7f8662


# def func(salt, s):
#     obj = hashlib.md5(salt)
#     obj.update(s.encode("utf-8"))
#     return obj.hexdigest()


# # 用户注册
# username = input("请输入用户名:")
# password = input("请输入密码:")
# #                    动态加盐
# mi_password = func(username.encode("utf-8"), password)
# f = open('user.txt', mode="w", encoding='utf-8')
# f.write(username)
# f.write("\n")
# f.write(mi_password)  # 把密文写出去

# # 登录
# username = input("用户名:")
# password = input("密码:")
# password = func(username.encode("utf-8"), password)
# f = open("user.txt", mode="r", encoding="utf-8")
# uname = f.readline().strip()
# upwd = f.readline().strip()
# # 需要把用户输入的明文加密之后, 再进行判断
# if username == uname and password == upwd:
#     print("登录成功")
# else:
#     print('登录失败')
#
# # md5一定要加盐. 否则容易撞库

# 文件也可以进行md5的加密操作
obj = hashlib.md5(b"abcdefg")
f = open('wf.txt', mode="rb")
for line in f:
    obj.update(line)

# 得到加密结果
print(obj.hexdigest())  # 981efc8315eee7b0e1ba4540565daae5


# 判断文件一致性
# 两个相同的文件的md5的值是一致的

# 在我们上传文件的时候, 首先计算你要上传的这个文件的md5. 拿着这个值去网盘的数据库中
# 搜索有没有相同的md5. 如果有. 直接就是已经上传过. 已经保存起来了.


