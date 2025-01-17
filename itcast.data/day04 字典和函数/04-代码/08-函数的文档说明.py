# 函数的文档说明本质就是注释,告诉别人,这个函数怎么使用的,是干什么事的
# 只不过这个注释，有特定的位置书写要求，要写在函数名字的下方


def func():
    """
    打印输出一个hello world,
    """
    # aaa
    print('hello wold')


func()
# 查看函数的文档注释可以使用help(函数名)
# help(print)

help(func)
