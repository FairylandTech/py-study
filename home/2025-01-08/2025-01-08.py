import time

def test_function(parm1:str,parm2:int):
    print(f"参数1：{parm1}")
    print(f'数字参数2：{parm2}')
'''
1. 写装饰器. 控制函数被调用的频率. 要求: 5秒钟执行一次. 少于5秒钟直接打印警告信息.
'''

excute_status = True
# def call_frequency(func):
#     def control(*args,**kwargs):
#         # func_name =
#         global excute_status
#         import time
#         if excute_status:
#             excute_status = False
#             result = func(*args,**kwargs)
#             time.sleep(5)
#             excute_status = True
#             return result
#         else:
#             print('距离上一次调用函数不足5秒')
#     return control


# def call_frequency(func):
#     def control(*args, **kwargs):
#         # func_name =
#         global excute_status
#         import time
#         if excute_status:
#             excute_status = False
#             start_time = time.time()
#             result = func(*args, **kwargs)
#             end_time = time.time()
#             if end_time - start_time >= 5:
#                 excute_status = True
#                 return result
#             else:
#                 print('距离上一次调用函数不足5秒')
#     return control


def call_frequency(excute_status: bool):
    def control(func):
        if excute_status == False:
            print('距离上一次调用函数不足5秒')

            def wrapper(*args, **kwargs):
                # func_name =
                global excute_status
                import time
                if excute_status:
                    excute_status = False
                    start_time = time.time()
                    result = func(*args, **kwargs)
                    end_time = time.time()
                    if end_time - start_time >= 5:
                        excute_status = True
                        return result
                    else:
                        print('距离上一次调用函数不足5秒')
                else:
                    print('距离上一次调用函数不足5秒')
            return wrapper
    return control

@call_frequency(excute_status = excute_status)
def test_function(parm1:str,parm2:int):
    print(f"参数1：{parm1}")
    time.sleep(2)
    print(f'数字参数2：{parm2}')

# test_function('self',55)
# test_function('self',55)


'''
2. 写装饰器. 通过一次调用使函数执行5次
'''


def reuse(func):
    def control(*args,**kwargs):
        for time in range(0,5):
            result = func(*args, **kwargs)
        return result
    return control

@reuse
def test_function(parm1:str,parm2:int):
    print(f"参数1：{parm1}")
    print(f'数字参数2：{parm2}')
# test_function('self',55)


'''
3. 写装饰器, 要求. 被装饰的函数在执行的时候首先要判断登录状态. 
如果是已经登录状态. 则直接执行. 否则提示用户去执行登录操作. 直到用户登录成功为止. 
'''


def judge_status(login_status:bool):
    def outer(func):

        def run(*args,**kwargs):
            if login_status:
                result = func(*args, **kwargs)
                return result
            else:
                print('当前未登录，请登录后操作')
                while True:
                    user_name = input('请输入用户名：')
                    user_password = input('请输入密码：')
                    if user_name == 'aa' and user_password == '123':
                        result = func(*args, **kwargs)
                        return result
                        break
                    else:
                        continue
        return run
    return outer


@judge_status(login_status = False)
def test_function(parm1:str,parm2:int):
    print(f"参数1：{parm1}")
    print(f'数字参数2：{parm2}')

# test_function('self',55)


'''
1)，启动程序，首页面应该显示成如下格式：
                欢迎来到博客园首页
                1:请登录
                2:请注册
                3:文章页面
                4:日记页面
                5:注销
                6:退出程序
2)，用户输入选项，3, 4选项必须在用户登录成功之后，才能访问成功。
3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，没成功则结束整个程序，
    登录成功之后，可以选择访问3, 4项，访问页面之前，必须要在log文件中打印日志，
    日志格式为 --> 用户:xx在xx年xx月xx日 执行了xxx函数，访问页面时，
    页面内容为：欢迎xx用户访问评论（文章，日记）页面
4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。
5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。
6)，退出程序为结束整个程序运行。

由于所有的操作都要带着用户名的. 比如, 查看sylar的文章. 打开的文件就是sylar_文章.txt. 
所以, 我们需要在登录的时候把用户名记录在全局变量中. 方便其他函数访问. 

其中进入文章和日记之后:
进入文章页面: 
    1. 查看文章
    2. 添加文章
    3. 删除文章
    4. 返回上一单元
    
进入日记页面: 
    1. 查看日记
    2. 添加日记
    3. 删除日记
    4. 返回单一单元
'''

import json
import os
from typing import List,Dict

encodeing = 'utf-8'
file_path = "user_information"
login_status = 0
user = False

def load_users(file_path: str) -> List[Dict[str,str]]:
    if os.path.isfile(file_path):
        return []
    with open(file_path,'r',encodeing) as user_information:
        data = json.load(user_information)

    return data

def save_user(file_path: str,data: List[Dict[str,str]]):
    try:
        with open(file_path,'w',encodeing) as user_information:
            datas = json.dump(data)
            user_information.write(datas)
            return True
    except Exception as e:
        print(e)
        return False


def register(name: str,password: str):
    data = load_users(file_path)
    user_dict = {
     "name":name,
     "password":password
    }
    datas = data.append(user_dict)
    if save_user(file_path,datas):
        global login_status
        global user
        login_status = 1
        user = name
        return True
    else:
        return False

def login(name: str,password: str):
    data = load_users(file_path)
    user_mapping = {user.get(name):user for user in data}

def main():
    while True:
        print('欢迎来到博客园首页')
        print('1:请登录')
        print('2:请注册')
        print('3: 文章页面')
        print('4: 日记页面')
        print('5: 注销')
        print('6: 退出程序')
        choice = int(input('请输入你的操作选择：'))
        if choice == 1:
            name = input('请输入你的登录用户名：')
            password = input('请输入你的登录密码：')

        elif choice == 2:
            name = input('请输入你的注册用户名：')
            password = input('请输入你的注册密码：')
            re_password = input('二次确认密码：')
            if password == re_password:
                if register(name,password):
                    print('注册成功')
            else:
                print('两次输入密码不一致，请重新输入：')

        elif choice == 3:
            print('欢迎xx用户访问评论文章页面')

        elif choice == 4:
            print('欢迎xx用户访问评论日记页面')

        elif choice == 5:
            global login_status
            global user
            login_status = 0
            user = False

        elif choice == 6:
            break

        else:
            print('输入选项有误，请重新输入')




if __name__ == '__main__':
    main()