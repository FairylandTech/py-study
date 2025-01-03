# # coding：utf-8
#
# # 操作系统：win， unix(内核)[ macOS(类unix系统)， linux （RedHat， Ubuntu，麒麟，鲲鹏， Android, IOS）]
# # 操作系统架构： x86 x86_64 arm x906
#
# # python解释器
# # 解释型语言，代码由上而下以此解释
# # 代码 -python 编译(内存)-> 机器码（二进制） --> 计算机处理 --> 输出结果
# # .py: python源代码
# # .pyc: python的字节码
# # .pyd: 编译后文件（win）
# # .so : 编译后文件(unix)
#
# # 注释：
# # 行注释： 代码开头：卸载代码的上方， # 后跟2个空格再开始写注释内容， 代码结尾：空1个空格在写#， #后面跟2个空格
# # 块注释： 在三个单/双引号内的注释都是块注释，一般出现在函数/类/模块开始的位置
# # 函数内部： 用来描述这个函数的主要功能
# # 类的内部： 用来描述这个类是用来干什么的， 主要实现了那些功能，有什么方法， 以及方法的简单使用
# # 模块的开始：用来描述这个模块是干什么的，什么时间实现的这个模块中的方法， 作者信息， 以及其他的模块信息
#
# # 变量
# # 临时存在计算机内存中
# # python中的变量命名规范：小写字母，多个单词用下划线（_）分割, 不可以数字/符号开头， 变量名不能包含符号，_除外
# var = 1
# a = 10
# b = 20
#
# # 全局变量
# # 命名规范：全部大写，多个单词用下划线（_）分割
# ROOT_PATH = "/root"
# NAMESPACE = "main"
#
# # 在计算机内存中python变量指向的是一个内存地址（0x00000001）而不是其本身
# #   ** 注意： Python中None（NoneType）的内存地址是固定的
# # 查看内存地址的方法：id()
# a_none = None
# b_none = None
# print(id(var), id(a_none), id(b_none))
# print(id(a_none) == id(b_none))
#
# # 内置变量 build-in
# import math
#
# print(math.e)
#
# # 常量 （通常是不变的，但是在python中，一切皆对象（都可变）） 只不过这样命名来区分（标识）是个常量
# # 全部大写字母
# PI = 3.14
#
# # 3.9 以下 流程控制：条件流程控制（if ... elif .. else ...）， 循环流程控制(for ..., while ..., switch ... case ...)
# # python 3.9 以后的版本加了 switch ... case ...
# """
# if 条件：
#     ...
#
# if 条件：
#     ...
# else：
#     ...
#
# if 条件：
#     ...
# elif 条件：
#     ...
# else：
#     ...
# """
#
# num = None
#
# if num:
#     print(num)
#
# if num:
#     print(num)
# else:
#     print("这是啥？？？")
#
# if num:
#     print(num)
# elif num == 1:
#     print("num 等于 1 。。。 嘻嘻")
# elif num == "1":
#     print("num 等于 1 。。。 嘻嘻")
# else:
#     print("不嘻嘻")
#
# print("if 程序运行结束")
#
# # 循环
# s = "aqoihqhoichnoasd"
# for i in s:
#     print(i)
#
# for _ in s:
#     print("aaaa")
#
# for i in range(10):  # 0-9
#     print(i)
#
# for i, c in enumerate("CHINA"):  # i: index 索引。 c: 迭代对象对应索引的值
#     print(i, c)
#
# for i in zip([1, 2], [10, 20]):  # zip(压缩为一个多维可迭代对象)
#     print(i)  # 元组
#
# for i, j in zip([1, 2], [10, 20]):  # zip(压缩为一个多维可迭代对象)
#     print(i, j)  # 元组
# #
# # for key, value in dict.items():
# #     pass
# #
# # a = [item for item in range(10)]
# # b = (item for item in range(10))
# # c = {item for item in range(10)}
# # d = {key: value for key, value in dict.items()}
#
# tuple_1 = (1, 2, 3)
# a, b, c = tuple_1
# print(a, b, c)
#
# a, *_ = tuple_1
# print(*_)
#
# a, _, c = tuple_1
# print(a, c)

########## 练习 ###########
"""
0. 规范
1. 数据类型： 字符串，整型，浮点，列表，元组，集合，字典
2. if流程控制语句
3. 单for循环
"""

'''
智能排序机器人
题目：
你现在公司的销售经理，要对一些销售数据进行分析
公司有百亿条销售数据，抽出一些销售额信息让你练手
sales = [100,200,50,300,20,500,1000,10]
(1)请对 sales 进行升序排序，并且打印出来
(2)请对 sales 进行降序排序，并且打印出来
(3)请用排序+切片的方式，找出 Top3 的销售额
(4)请用排序+切片的方式，找出 最低的3个销售额
'''

sales = [100,200,50,300,20,500,1000,10]
sales.sort(reverse=True)
print(sales)
#Top3 的销售额
print(sales[0:3])

sales.sort(reverse=False)
print(sales)
#最低的3个销售额
print(sales[0:3])

'''车位管理机器人
题目：
你现有管理一个停车场
现有一组车位租用情况，结构如下：
car_nums = ['A0001','A00X9','A0027']   
(1)现有新来了一辆车 'A0030', 请把它放在 car_nums 的最后面
(2)现有新来了一辆车 'A0000', 请把它放在 car_nums 的最前面
(3)'A00X9' 这辆车现在不租你的停车位上，请把它从 car_nums 中删掉
(4)现在来了一个车队 ['B0001','B0002','B003'], 请用一行代码把它加到 car_nums 中'''

car_nums = ['A0001','A00X9','A0027']
#(1)现有新来了一辆车 'A0030', 请把它放在 car_nums 的最后面
car_nums.append('A0030')
print(car_nums)
#(2)现有新来了一辆车 'A0000', 请把它放在 car_nums 的最前面
car_nums.insert(0, 'A0000')
print(car_nums)
#(3)'A00X9' 这辆车现在不租你的停车位上，请把它从 car_nums 中删掉
car_nums.remove('A00X9')
# car_nums = car_nums.pop(2)
print(car_nums)
#(4)现在来了一个车队 ['B0001','B0002','B003'], 请用一行代码把它加到 car_nums 中'''
car_nums.extend(['B0001','B0002','B003'])
print(car_nums)


'''自动询价机器人
题目：
你现在管理一个商务团队，每天有客户找问价格
你有一个价格对应表
  prices =  {
      "SKU-A": 100,
      "SKU-B": 120,
      "SKU-C": 190,
      "SKU-D": 200
  }
每次客户来问题，你都要找这个表，你现在很烦，想做一个自动机器人
1.写一个 while 循环，提示用户输入 sku
2.根据用户输入的sku查询 prices, 找印出对应价格
3.如果用户输入 ! 则退出循环(break)'''
prices = {
    "SKU-A": 100,
    "SKU-B": 120,
    "SKU-C": 190,
    "SKU-D": 200
}
while True:
    things = input('请输入您想咨询的商品（按![英文的]结束咨询）：')
    if things !='!':
        if prices.get(things) == None:
            print('您咨询的商品暂未上架')
        else:
            print(f'{things}的价格是：'+str(prices.get(things))+'元')
    else:
        print('感谢您的来访，再见！')
        break


'''仓库数据管理机器人
题目：
你现在是仓库的负责人
仓库数格式是这样的
    total = [
        {"sku": "SKU-A", "quantity": 100},
        {"sku": "SKU-B", "quantity": 200},
        {"sku": "SKU-C", "quantity": 400},
        {"sku": "SKU-D", "quantity": 300},
    ]
1.请统计仓库的物品总数量(quantity)
2.现在 SKU-A 要入库 100件商品，请更新 SKU-A 的库存记录
3.现在 SKU-E 新品上市，要入库300件商品，请在 total 中新增一条相应记录
4.现在 SKU-B 要退市，请将 SKU-B 这行记录删掉 #此题可选
5.使用切片方法显示 total 中的最后一行记录'''
total = [
    {"sku": "SKU-A", "quantity": 100},
    {"sku": "SKU-B", "quantity": 200},
    {"sku": "SKU-C", "quantity": 400},
    {"sku": "SKU-D", "quantity": 300},
]
#1请统计仓库的物品总数量(quantity)
num = 0
for int in total:
    num += int["quantity"]
print(num)

#2.现在 SKU-A 要入库 100件商品，请更新 SKU-A 的库存记录
# total[0]["quantity"] = total[0]["quantity"]+100
total[0]["quantity"] += 100
print(total[0]["quantity"])
# print(total[0])

#3.现在 SKU-E 新品上市，要入库300件商品，请在 total 中新增一条相应记录
total.append({"sku": "SKU-E", "quantity": 300})
print(total)

#4.现在 SKU-B 要退市，请将 SKU-B 这行记录删掉 #此题可选
# total.pop(1)
total.remove({"sku": "SKU-B", "quantity": 200})
print(total)

#5.使用切片方法显示 total 中的最后一行记录'''
print(total[-1])