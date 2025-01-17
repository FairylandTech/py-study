# __all__ = ['num', 'func']
__all__ = ('num', 'func')

num = 3


def func():
    print('my_module3  func .....')


class Dog(object):
    @staticmethod
    def show_info():
        print('这是一个Dog类 , my_module3 dog类')
    pass

