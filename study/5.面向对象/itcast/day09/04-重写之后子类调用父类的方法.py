# 1. 定义Dog类, 书写bark方法, 输出 汪汪汪叫
class Dog(object):
    def bark(self):
        print('汪汪汪叫.........')


# 2. 定义XTQ类,继承Dog类. 重写父类中的bark方法, 输出 嗷嗷嗷叫
class XTQ(Dog):
    def bark(self):
        print('嗷嗷嗷叫--------')

    def see_host(self):
        """看见主人之后,要汪汪汪叫,不能嗷嗷嗷叫"""
        print('看见主人了,', end='')
        # self.bark()
        # 想要在子类中调用父类的同名方法
        # 方法一: 父类名.方法名(self, 其他参数), 通过实例对象.方法名() 调用方法,不需要给self传递实参值,
        # python解释器会自动将对象作为实参值传递给self形参, 如果是通过类名.方法() 调用,python解释器就
        # 不会自动传递实参值,需要手动给self形参传递实参值
        Dog.bark(self)

        # 方法二  super(类A, self).方法名(参数) , 会调用当类A 的父类中的方法
        super(XTQ, self).bark()  # 调用 XTQ类父类中的bark方法

        # 方法三  是方法二的简写, super().方法名(参数) ==> super(当前类, self).方法名()
        super().bark()


# 创建XTQ类对象
xtq = XTQ()
xtq.see_host()