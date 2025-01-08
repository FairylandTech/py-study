def test_function(parm1:str,parm2:int):
    print(f"参数1：{parm1}")
    print(f'数字参数2：{parm2}')

'''
1. 写装饰器. 控制函数被调用的频率. 要求: 5秒钟执行一次. 少于5秒钟直接打印警告信息.
'''

excute_status = True
def call_frequency(func):
    def control(*args,**kwargs):
        # func_name =

        global excute_status
        import time
        if excute_status:
            excute_status = False
            start_time = time.time()
            result = func(*args,**kwargs)
            end_time = 
            excute_status = True
            return result
        else:
            print('距离上一次调用函数不足5秒')
    return control



@call_frequency
def test_function(parm1:str,parm2:int):
    print(f"参数1：{parm1}")
    print(f'数字参数2：{parm2}')

test_function('self',55)
test_function('self',55)


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


# def judge_status(login_status:bool)


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