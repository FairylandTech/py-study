# a = 10
#
#
# def func():
#     global a  # 当前func函数内部使用的a都是全局的
#     a = a + 1
#     print(a)
#
#
# func()
# print(a)





# a = 10
# def func():
#     global a  # 把全局内容引入到局部
#     a = 20
#     print(a)
#
# print(a)  # 10
# func()
# print(a)

# def func1():
#     a = 10
#     def func2():
#         nonlocal a  # 必须在局部, 把外层中的xxx变量引入进来
#         a += 1
#         print(a)
#     func2()
#     print(a)
#
# func1()
#
# # 只要出现了, 在局部中改变外层变量, 就需要使用global或者nonlocal


flag = False
def login():
    global flag
    username = input(">>>:")
    password = input(">>>:")
    if username == "sylar" and password == '123':
        print("登录成功")
        flag = True
    else:
        print("登录失败")

def add():
    if flag:
        pass
    else:
        print("没登录呢. 请登录..")

def upd():
    pass

def delete():
    pass

def search():
    pass


