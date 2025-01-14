import time

from anaconda_navigator.utils.url_utils import file_name


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
user = None

def load_users(file_path: str) -> List[Dict[str,str]]:
    if not os.path.isfile(file_path):
        return []
    with open(file_path,'r',encoding=encodeing) as user_information:
        data = json.load(user_information)

    return data

def save_user(file_path: str,data: List[Dict[str,str]]):
    try:
        with open(file_path,'w',encoding=encodeing) as user_information:
            # datas = json.dump(data)
            # user_information.write(datas)
            json.dump(data,user_information)
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
    # datas = data.append(user_dict)
    data.append(user_dict)
    if save_user(file_path,data):
        global login_status
        global user
        login_status = 1
        user = name
        return True
    else:
        login_status = 0
        user = None
        return False

def login(name: str,password: str):
    data = load_users(file_path)
    user_mapping = {user.get("name"):user for user in data}
    if user_mapping.get(name) is not None:
        user_information = user_mapping.get(name)
        num = 0
        while num <= 3:
            if name == user_information.get(name) and password == user_information.get(password):
                global login_status
                global user
                login_status = 1
                user = name
                return True
                break
            else:
                login_status = 0
                user = None
                num += 1
                return False
def read_article(article_name: str):
    file_name = user + '文章' + article_name+ '.txt'
    with open(file_name,'r',encodeing) as article_information:
        article = article_information.read()
        if article:
            return article
        else:
            return None

def write_article(article_name: str,article_data: str):
    file_name = user + '文章' + article_name + '.txt'
    with open(file_name,'w',encodeing) as article_information:
        article_information.write(article_data)
        return True

def delete_article(article_name: str):
    file_name = user + '文章' + article_name+ '.txt'
    os.remove(file_name)
    return True

def read_diary(diary_name: str):
    file_name = user + '日记' + diary_name + '.txt'
    with open(file_name,'r',encodeing) as diary_information:
        diary = diary_information.read()
        if diary:
            return diary
        else:
            return None

def write_diary(diary_name: str,diary_data: str):
    file_name = user + '日记' + diary_name + '.txt'
    with open(file_name,'w',encodeing) as diary_information:
        diary_information.write(diary_data)
        return True

def delete_diary(diary_name: str):
    file_name = user + '日记' + diary_name + '.txt'
    os.remove(file_name)
    return True

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
            if login_status == 0:
                name = input('请输入你的登录用户名：')
                password = input('请输入你的登录密码：')
                if login(name,password):
                    print(f'登录成功，欢迎您{user}!')
                else:
                    print('用户名或密码错误，请重新登录')
            else:
                print('您当前已经登录，无需登录')

        elif choice == 2:
            if login_status == 0:
                name = input('请输入你的注册用户名：')
                password = input('请输入你的注册密码：')
                re_password = input('二次确认密码：')
                if password == re_password:
                    if register(name,password):
                        print('注册成功')
                    else:
                        print('注册失败')
                else:
                    print('两次输入密码不一致，请重新输入：')
            else:
                print('您当前已经登录，请注销后在注册')

        elif choice == 3:
            if login_status == 1:
                while True:
                    print(f'欢迎{user}用户访问评论文章页面')
                    print('1.查看文章')
                    print('2.添加文章')
                    print('3.删除文章')
                    print('4.返回上一单元')
                    choice = int(input('请输入你的操作选择：'))
                    if choice == 1:
                        file_name = input('请输入你想查看的文章名')
                        article =  read_article(file_name)
                        if article:
                            print(article)
                        else:
                            print('没有找到这篇文章')
                    elif choice == 2:
                        file_name = input('请输入你添加的文章名:')
                        article = input('请输入你的文章内容：')
                        result = write_article(file_name,article)
                        if result:
                            print('添加成功')
                        else:
                            print('添加失败')
                    elif choice == 3:
                        file_name = input('请输入你删除的文章名:')
                        delete_article(file_name)
                        print('删除成功！')
                    elif choice == 4:
                        break
            else:
                print('您当前未登录，请登录后再来')


        elif choice == 4:
            if login_status == 1:
                while True:
                    print('欢迎xx用户访问评论日记页面')
                    print('1.查看日记')
                    print('2.添加日记')
                    print('3.删除日记')
                    print('4.返回单一单元')
                    choice = int(input('请输入你的操作选择：'))
                    if choice == 1:
                        file_name = input('请输入你想查看的日记名')
                        diary = read_diary(file_name)
                        if diary:
                            print(diary)
                        else:
                            print('没有找到这篇日记')
                    elif choice == 2:
                        file_name = input('请输入你添加的日记名:')
                        diary = input('请输入你的日记内容：')
                        result = write_article(file_name, diary)
                        if result:
                            print('添加成功')
                        else:
                            print('添加失败')
                    elif choice == 3:
                        file_name = input('请输入你删除的日记名:')
                        delete_diary(file_name)
                        print('删除成功！')
                    elif choice == 4:
                        break
            else:
                print('您当前未登录，请登录后再来')


        elif choice == 5:
            global login_status
            global user
            login_status = 0
            user = False
            print('注销成功')

        elif choice == 6:
            break

        else:
            print('输入选项有误，请重新输入')




if __name__ == '__main__':
    main()