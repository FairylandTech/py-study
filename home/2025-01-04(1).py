'''
基于字典的客户信息管理系统             -------------------------------------------------------------
           1. 添加客户
           2. 删除客户
           3. 修改客户
           4. 查询一个客户
           5. 查询所有客户
           6. 退出
name = input("请输入添加客户的姓名:")
age = input("请输入添加客户的年龄:")
email = input("请输入添加客户的邮箱:")
'''

# #非持久化
#
# customer_information = {}
# while True:
#     print('''功能编号如下：
#                1. 添加客户
#                2. 删除客户
#                3. 修改客户
#                4. 查询一个客户
#                5. 查询所有客户
#                6. 退出''')
#     operate = int(input("请输入您想进行的操作："))
#
#     if operate ==1:
#         name = input("请输入添加客户的姓名:")
#         age = input("请输入添加客户的年龄:")
#         email = input("请输入添加客户的邮箱:")
#         customer_information[name] = {"姓名":name,"年龄":age,"邮箱":email}
#         print(customer_information)
#     elif operate == 2:
#             try:
#                 customer = input('请输入想删除的客户姓名：')
#
#                 if customer_information[customer] is not None:
#                     customer_information.pop(customer)
#                     print('删除成功！')
#             except Exception as e:
#                     while True:
#                         customer = input("没有找到这个客户，请输入正确的客户名(按1返回上一级菜单栏)：")
#                         try:
#                             if int(customer) == 1:
#                                 break
#                         except Exception as e:
#                             try:
#                                 if customer_information[customer] is not None:
#                                     customer_information.pop(customer)
#                                     print('删除成功！')
#                                     break
#                             except Exception as e:
#                                     continue
#
#     elif operate == 3:
#         customer = input("请输入您想修改的客户的姓名:")
#         try:
#             if customer_information[customer] is not None:
#                 name = input("请输入修改后的客户的姓名:")
#                 age = input("请输入修改的后客户的年龄:")
#                 email = input("请输入修改后的客户的邮箱:")
#                 # information = customer_information[customer]
#                 before = customer_information.pop(customer)
#                 customer_information[name] = {"姓名": name, "年龄": age, "邮箱": email}
#                 after = customer_information[name]
#                 print(f'修改成功，客户{before}现在为{after}')
#                 # print(information)
#         except Exception as e:
#                 while True:
#                     customer = input("没有找到这个客户，请输入正确的客户名(按1返回上一级菜单栏)：")
#                     try:
#                         if int(customer) == 1:
#                             break
#                     except Exception as e:
#                         try:
#                             if customer_information[customer] is not None:
#                                 name = input("请输入修改后的客户的姓名:")
#                                 age = input("请输入修改的后客户的年龄:")
#                                 email = input("请输入修改后的客户的邮箱:")
#                                 # information = customer_information[customer]
#                                 before = customer_information.pop(customer)
#                                 customer_information[name] = {"姓名": name, "年龄": age, "邮箱": email}
#                                 after = customer_information[name]
#                                 print(f'修改成功，客户{before}现在为{after}')
#                                 # print(information)
#                                 break
#                         except Exception as e:
#                                 continue
#     elif operate == 4:
#         customer = input('请输入想查询的客户姓名：')
#         try:
#             if customer_information[customer] is not None:
#                 information = customer_information[customer]
#                 print(information)
#         except Exception as e:
#             while True:
#                 try:
#                     customer = input("没有找到这个客户，请输入正确的客户名(按1返回上一级菜单栏)：")
#                     if int(customer) == 1:
#                         break
#                 except Exception as e:
#                     try:
#                         if customer_information[customer] is not None:
#                             information = customer_information[customer]
#                             print(information)
#                             break
#                     except Exception as e:
#                         continue
#
#     elif operate == 5:
#         print(customer_information.items())
#
#     elif operate == 6:
#         break
# print(customer_information)


#持久化

customer_information = {}
while True:
    print('''功能编号如下：
               1. 添加客户
               2. 删除客户
               3. 修改客户
               4. 查询一个客户
               5. 查询所有客户
               6. 退出''')
    operate = int(input("请输入您想进行的操作："))

    if operate ==1:
        name = input("请输入添加客户的姓名:")
        age = input("请输入添加客户的年龄:")
        email = input("请输入添加客户的邮箱:")
        with open ('客户信息.txt','a',encoding='utf-8') as information:
            information.write(f'"姓名":{name},"年龄": {age},"邮箱": {email}\n')

    elif operate == 2:
            try:
                customer = input('请输入想删除的客户姓名：')

                if customer_information[customer] is not None:
                    customer_information.pop(customer)
                    print('删除成功！')
            except Exception as e:
                    while True:
                        customer = input("没有找到这个客户，请输入正确的客户名(按1返回上一级菜单栏)：")
                        try:
                            if int(customer) == 1:
                                break
                        except Exception as e:
                            try:
                                if customer_information[customer] is not None:
                                    customer_information.pop(customer)
                                    print('删除成功！')
                                    break
                            except Exception as e:
                                    continue

    elif operate == 3:
        customer = input("请输入您想修改的客户的姓名:")
        try:
            if customer_information[customer] is not None:
                name = input("请输入修改后的客户的姓名:")
                age = input("请输入修改的后客户的年龄:")
                email = input("请输入修改后的客户的邮箱:")
                # information = customer_information[customer]
                before = customer_information.pop(customer)
                customer_information[name] = {"姓名": name, "年龄": age, "邮箱": email}
                after = customer_information[name]
                print(f'修改成功，客户{before}现在为{after}')
                # print(information)
        except Exception as e:
                while True:
                    customer = input("没有找到这个客户，请输入正确的客户名(按1返回上一级菜单栏)：")
                    try:
                        if int(customer) == 1:
                            break
                    except Exception as e:
                        try:
                            if customer_information[customer] is not None:
                                name = input("请输入修改后的客户的姓名:")
                                age = input("请输入修改的后客户的年龄:")
                                email = input("请输入修改后的客户的邮箱:")
                                # information = customer_information[customer]
                                before = customer_information.pop(customer)
                                customer_information[name] = {"姓名": name, "年龄": age, "邮箱": email}
                                after = customer_information[name]
                                print(f'修改成功，客户{before}现在为{after}')
                                # print(information)
                                break
                        except Exception as e:
                                continue
    elif operate == 4:
        customer = input('请输入想查询的客户姓名：')
        try:
            # if customer_information[customer] is not None:
                with open('客户信息.txt','r',encoding='utf-8') as information:
                    informations = information.readlines()
                    # while customer in informations:
                    print(informations)
                    # print(repr(informations))
                    print(type(informations))

                    for i in informations:
                        # print(i)
                        # print(repr(i))
                        # print(type(i))
                        if customer in i:
                            index = informations.index(i)
                            print(informations[index])

            # information = customer_information[customer]
            # print(information)
        except Exception as e:
            while True:
                try:
                    customer = input("没有找到这个客户，请输入正确的客户名(按1返回上一级菜单栏)：")
                    if int(customer) == 1:
                        break
                except Exception as e:
                    try:
                        if customer_information[customer] is not None:
                            information = customer_information[customer]
                            print(information)
                            break
                    except Exception as e:
                        continue

    elif operate == 5:
        print(customer_information.items())

    elif operate == 6:
        break
print(customer_information)



# # # customer_information = {'aa':{'姓名': 'aa', '年龄': 'asd', '邮箱': 'asd'},'ad':{'姓名': 'ad', '年龄': 'asd', '邮箱': 'asd'}}
# # # customer_information = {'aa':'asdsd', 'ad':'dgfs'}
# # name = input("请输入添加客户的姓名:")
# # age = input("请输入添加客户的年龄:")
# # email = input("请输入添加客户的邮箱:")
# # customer_information = {}
# #
# # customer_information[name] = {"姓名":name,"年龄":age,"邮箱":email}
# # print(customer_information)
# # b = input('查询')
# # c = input('改后')
# # a = customer_information["aa"]
# # print(a)
# # print(a['姓名'])
# # a = customer_information[b]
# # print(a)
# # print(a.get("aa"))
# # print(a.items())
# # # print(a[c])
# # a = customer_information['aa']
# # print(a)
#
#
# '''
# 示例：计算BMI并给出健康建议           -------------------------------------------------------
# '''
#
# height = float(input('请输入您的身高(单位：米)：'))
# weight = float(input('请输入您的体重(单位：千克)：'))
# bmi = weight/height**2
# if bmi < 18.5 :
#     print(f'您的bmi（体重指数）为{bmi},有些偏轻，建议增加体重。')
# elif 18.5 <= bmi <= 24:
#     print(f'您的bmi（体重指数）为{bmi},正常状态，维持体重就好。')
# elif 24 < bmi <= 28:
#     print(f'您的bmi（体重指数）为{bmi},有些超重，需要适当减肥了。')
# else:
#     print(f'您的bmi（体重指数）为{bmi},属于肥胖，必须要减肥了。')
#



# '''
# 场景：
# （1）怪物房： 遇到了史莱姆，并打败了它，金币加5，经验加10！      ----------------------------------
# (2) 宝箱房: 你打开了宝箱，获得了钥匙
# (3) 陷阱房: 你触发了陷阱，受到了毒箭的伤害,血值减10
# (4) 商店:   你来到了商店，购买了药水,金币减5，血值加20
# '''
#
#
# import random
#
# print('欢迎勇者进入游戏！')
# experience = 0
# money = 20
# hp = 100
# print(f'你的初始血量为{hp}，金币数量为{money}，经验值为{experience}')
#
#
# choice = random.randint(1,4)
# # print(choice)
# if choice == 1:
#     print('你进入了怪物房，遇到了史莱姆，并打败了它，金币加5，经验加10！')
#     money += 5
#     experience += 10
#     print(f'你当前血量为{hp}，金币数量为{money}，经验值为{experience}')
# elif choice == 2:
#     print('你进入了宝箱房,你打开了宝箱，获得了钥匙')
#     print(f'你当前血量为{hp}，金币数量为{money}，经验值为{experience}')
# elif choice == 3:
#     print('你进入了陷阱房,你触发了陷阱，受到了毒箭的伤害,血值减10')
#     hp -= 10
#     print(f'你当前血量为{hp}，金币数量为{money}，经验值为{experience}')
# else:
#     print('你进入了商店,你来到了商店，购买了药水,金币减5，血值加20')
#     money -= 5
#     hp += 20
#     print(f'你当前血量为{hp}，金币数量为{money}，经验值为{experience}')


'''
"""
 勇士与地下城的场景续写：
（1）怪物房： 遇到了史莱姆
                1. 选择攻击，战胜史莱姆，则经验加20，金币加20，失败则经验减20，金币减20，血值减20，成功的概率为50%。
                2. 选择逃跑，则金币减20
 (2) 宝箱房: 你打开了宝箱，获得了钥匙
 (3) 陷阱房: 你触发了陷阱，受到了毒箭的伤害,血值减10
 (4) 商店:   你来到了商店，打印当前血值和金币，一个金币买一个药水对应10个血值，引导是否购买药水
                1. 购买，引导购买几个金币的药水，并完成减金币和增血值
                2. 不购买，打印退出商店

"""
'''

# import random
#
# print('欢迎勇者进入游戏！')
# experience = 100
# money = 50
# hp = 100
# print(f'你的初始血量为{hp}，金币数量为{money}，经验值为{experience}')
#
#
# choice = random.randint(1,4)
# # print(choice)
# if choice == 1:
#     print('''你进入了怪物房，遇到了史莱姆，
#     1. 选择攻击，战胜史莱姆，则经验加20，金币加20，失败则经验减20，金币减20，血值减20，成功的概率为50%。
#     2. 选择逃跑，则金币减20''')
#     choices = int(input('请输入你的选择：'))
#     if choices == 1:
#         result = random.randint(1, 2)
#         if result == 1:
#             money += 20
#             experience += 20
#             print(f'你战胜了史莱姆，经验加20，金币加20，你当前血量为{hp}，金币数量为{money}，经验值为{experience}')
#         elif result == 2:
#             money -= 20
#             experience -= 20
#             hp -= 20
#             print(f'你失败了，经验减20，金币减20，血值减20，你当前血量为{hp}，金币数量为{money}，经验值为{experience}')
#     else:
#         money -= 20
#         print(f'你逃跑了，则金币减20，你当前血量为{hp}，金币数量为{money}，经验值为{experience}')
#
# elif choice == 2:
#     print('你进入了宝箱房,你打开了宝箱，获得了钥匙')
#     print(f'你当前血量为{hp}，金币数量为{money}，经验值为{experience}')
# elif choice == 3:
#     print('你进入了陷阱房,你触发了陷阱，受到了毒箭的伤害,血值减10')
#     hp -= 10
#     print(f'你当前血量为{hp}，金币数量为{money}，经验值为{experience}')
# else:
#     print(f'''你来到了商店，你当前血量为{hp}，金币数量为{money}。
#             请问是否购买药水（一个金币买一个药水增加10点血量）''')
#     buy = int(input('请输入你的选择( 1.购买 2.不购买)：'))
#     if buy == 1:
#         buy_water = int(input("请问你要买几瓶："))
#         money -= buy_water
#         hp += buy_water*10
#         print(f'你当前血量为{hp}，金币数量为{money}，经验值为{experience}')
#     else:
#         print('退出商店')

'''
案例2：验证码案例
假设有一个变量s的初始值为""，将s拼接5次，每次增加值分别为"A"，"B"，"C"，然后打印s的值。    -----------------
'''

# import string
# import random
#
# auth_code = ''
# # auth_code.join(random.choice(string.ascii_letters))
# # auth_code.join(random.choice(string.digits))
# # auth_code.join(random.choice(string.ascii_letters))
# # auth_code.join(random.choice(string.digits))
# # auth_code.join(random.choice(string.ascii_letters))
# auth_code += random.choice(string.ascii_letters)
# auth_code += random.choice(string.digits)
# auth_code += random.choice(string.ascii_letters)
# auth_code += random.choice(string.digits)
# auth_code += random.choice(string.ascii_letters)
# print(auth_code)


'''
案例4：打印扑克牌
poke_types = ['♥️', '♦️', '♠️', '♣️']
poke_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']   ------------------------------------
'''
# poke_types = ['♥️', '♦️', '♠️', '♣️']
# poke_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
# for flower in poke_types:
#     for nums in poke_nums:
#         poke = flower + str(nums)
#         print(poke)


# '''
# 案例1: 构建一个列表，存储1-10的平方值       ---------------------------------------------------
# '''
# square_list = [i**2 for i in range(1,11) ]
# print(square_list)

