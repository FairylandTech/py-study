"""
私有方法: 在方法的前边加上两个__ ,就为私有方法
私有方法,不能在类外部访问
作用: 一般作为类内部的方法使用,不让在外部直接调用, 保证业务逻辑不被破坏
"""


class Dog(object):
    def born(self):
        """生小狗的方法, 生一个小狗,休息30天"""
        print('生了一只小狗...')
        self.__sleep()

    def __sleep(self):
        print('休息30天')


dog = Dog()
# dog.__sleep()
dog.born()
