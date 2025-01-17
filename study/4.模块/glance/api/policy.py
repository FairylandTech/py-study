"""
绝对导入, 绝对于整个包. 你要导入的模块位置
相对导入, 相对与当前文件所在位置,
    . 当前包
    .. 上一层包

    可能会出现问题
        如果启动在包内: 有可能会出问题
        如果再包外启动: 此时就没问题

    解决方案:
        1. 尽量用绝对导入
        2. 尽量在包外面启动程序
"""
# from glance.cmd import manage
from ..cmd import manage
def get():
    print('policy')
    manage.func()

if __name__ == '__main__':
    get()   # 在包内启动该程序.没报错


"""
包 -> 模块 -> 类 -> 函数 -> 语句
"""
