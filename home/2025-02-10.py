# '''
# 题目1 [加强训练]
# 题干
# 定义一个Star类(明星类)，通过明星类创建一个zhou_xing_chi对象。
# 训练目标
# 类的定义
# 创建对象
#
# 给对象添加属性
# 明星姓名=“周星驰”
# 明星的电影=“功夫”
# 使用init方法给对象添加name 和 movie属性
# 使用init方法给对象添加属性
# 定义方法playing()，打印“xxx出演了yyy，非常好看”
# 使用init方法给对象添加属性
# print输出对象时打印"xxx是我的偶像，我非常喜欢他的电影yyy"
# xxx为明星姓名，yyy是电影的名字
# 使用init方法给对象添加属性
# 删除创建的对象，打印“我不喜欢xxx了”
# '''
#
# # class Star():
# #     def __init__(self,name,movie):
# #        self.name = name
# #        self.movie = movie
# #
# #     def __str__(self):
# #         return f'{self.name} 是我的偶像，我非常喜欢他的电影{self.movie}'
# #
# #     def __del__(self):
# #         print(f"{self.name}我不再喜欢了")
# #
# #     def playing(self,):
# #         print(f"{self.name}出演了{self.movie}，非常好看")
# #
# #
# # zhou_xing_chi = Star('周星驰','功夫')
# # zhou_xing_chi.playing()
# # print(zhou_xing_chi)
#
# '''
# a.定义一个Star类(明星类)，包含初始化init方法：
# 成员属性：明星姓名
# 明星的电影
# 成员方法：playing()
# 打印：“xxx出演了yyy，非常好看”
# 打印对象时显示“xxx是我的偶像，我非常喜欢他的电影yyy”
# 删除对象提示“xxx我不再喜欢了”
# xxx为明星姓名，yyy是电影的名字
# b.键盘循环输入五个Star对象的姓名和电影名。
# c.分别调用输入Star对象的playing方法和打印对象
#
# 请输入你喜欢的明星:周星驰
# 请输入电影名功夫
# 请输入你喜欢的明星:刘德华
# 请输入电影名狄仁杰
# 请输入你喜欢的明星:周润发
# 请输入电影名赌神
# 周星驰出演了功夫，非常好看
# 周星驰是我的偶像，我非常喜欢他的电影功夫
# 刘德华出演了狄仁杰，非常好看
# 刘德华是我的偶像，我非常喜欢他的电影狄仁杰
# 周润发出演了赌神，非常好看
# 周润发是我的偶像，我非常喜欢他的电影赌神
# 我不喜欢周星驰了
# 我不喜欢刘德华了
# 我不喜欢周润发了
# '''
#
# class Star():
#     def __init__(self,name,movie):
#        self.name = name
#        self.movie = movie
#
#     def __str__(self):
#         return f'{self.name} 是我的偶像，我非常喜欢他的电影{self.movie}'
#
#     def __del__(self):
#         print(f"{self.name}我不再喜欢了")
#
#     def playing(self,):
#         print(f"{self.name}出演了{self.movie}，非常好看")
#
# staus = {}
# for i in range(3):
#     name = input('请输入你喜欢的明星:')
#     movie = input('请输入电影名:')
#     staus.update({name:movie})
#
# for name,movie in staus.items():
#         star = Star(name,movie)
#         star.playing()
#         print(star)
#
# staus = {}
# i = 0
# while i < 3:
#     name = input('请输入你喜欢的明星:')
#     movie = input('请输入电影名:')
#     staus.update({name:movie})
#     i += 1
# for name,movie in staus.items():
#         star = Star(name,movie)
#         star.playing()
#         print(star)
#
# # count = input('请输入需要一次输入多少位明星：')
# # count = int(count)
# # staus = {}
# # for i in range(count):
# #     name = input('请输入你喜欢的明星:')
# #     movie = input('请输入电影名:')
# #     staus.update({name: movie})
# #
# # for name, movie in staus.items():
# #     star = Star(name, movie)
# #     star.playing()
# #     print(star)



'''
继承


1. 创建一个Animal（动物）基类,其中有一个run方法,输出`跑起来....`
2. 创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法
    1. run方法输出 `跑起来....`
    2. eat 方法输出 `吃东西...`
'''

class Animal:
    def run(self):
        print('跑起来....')

class Horse(Animal):
    def eat(self):
        print('吃东西...')

horse = Horse()
horse.run()
horse.eat()
'''
创建一个动物(Animal)的基类,其中有一个run方法, 输出`跑起来....`

创建一个Horse（马）类继承于动物类，Horse类中重写run方法，增加打印输出"迈着矫健的步伐跑起来"，同时实现eat方法, 输出 `吃东西...`
'''
class Animal:
    def run(self):
        print('跑起来....')

class Horse(Animal):
    def run(self):
        print('迈着矫健的步伐跑起来')

    def eat(self):
        print('吃东西...')

horse = Horse()
horse.run()
horse.eat()

'''
1. 创建一个动物(Animal)的基类,其中有一个run方法, 输出`跑起来....`
2. 创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法
    1. run方法输出 `跑起来....`
    2. eat 方法输出 `吃东西...`
3. 创建一个 SwiftHorse（千里马）类继承Horse类，初始化init方法name属性为千里马
'''
class Animal:
    def run(self):
        print('跑起来....')

class Horse(Animal):
    def eat(self):
        print('吃东西...')

class SwiftHorse(Horse):
    def __init__(self):
        self.name = '千里马'

swift_horse = SwiftHorse()
swift_horse.run()
swift_horse.eat()
print(swift_horse.name)