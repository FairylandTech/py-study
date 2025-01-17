import random

while True:
    # 1. 用户输入自己出拳的内容
    user = int(input('请输入要出的拳:1(石头) 2(剪刀) 3(布):'))
    # 2. 让电脑随机出拳
    computer = random.randint(1, 3)  # 随机产生1-3 之间的随机数
    # print(computer)
    # 3. 判断胜负
    # 3.1 平局 输入的内容一样  user == computer
    # 3.2 user 胜利, ①. user==1 and computer==2  ② user==2 and computer==3 ③ user==3 and computer == 1
    # 3.3 else 剩下的情况就是电脑胜利
    if user == computer:
        print('平局')
    elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
        print('恭喜你,胜利了')
    else:
        print('你输了,弱爆了')



