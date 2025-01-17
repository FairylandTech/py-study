"""
私有属性,只需要在原属性名前加上两个下划线,即可
目的: 保证数据的相对安全,
想要访问和使用私有属性: 定义一个公有的方法,通过这个方法使用
"""


# 案例需求: 定义People 类, 定义属性 ICBC_money , 钱不能随便被修改,必须是合法的终端才可以操作
class People(object):
    def __init__(self):
        # python中的私有本质是 修改属性的名字, 在创建对象的时候,会自动的修改属性名
        # 在属性名的前边加上 _类名前缀
        self.__ICBC_money = 0  # 定义私有属性

    # 定义公有的方法,提供接口,修改余额
    def get_money(self):
        return self.__ICBC_money

    def set_money(self, money):
        num = input('输入金额:')
        self.__ICBC_money += int(num)
        # self.__ICBC_money += money

# 创建People类对象
xw = People()
# 实例对象.__dict__  可以查看对象具有的属性信息,类型是字典,字典的key是属性名, 字典的value是属性值
print('赋值之前:', xw.__dict__)
# print(xw.__ICBC_money)
xw.__ICBC_money = 1000  # 不是修改私有属性,是重新添加一个公有属性
print('赋值之后:', xw.__dict__)
print(xw.__ICBC_money)
print('=' * 20)
print(xw.get_money())  # 0
xw.set_money(1000)
print(xw.get_money())  # 1000
xw.set_money(-500)
print(xw.get_money())  # 500


