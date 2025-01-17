def func1():
    print('-------1---------')
    num = input('请输入数字')  # 0
    num = 10 / int(num)  # 假设0 是计算的出来的
    print(num)
    print('-------2---------')


def func2():
    print('-------3---------')
    func1()
    print('-------4---------')


try:
    print('-------5---------')
    func2()
    print('-------6---------')
except Exception as e:
    print('-------7---------')
    print(e)

# 5 3 1 7

