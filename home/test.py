# dict_test = dict()
# key4 = "key4.4"
# dict_test.update(key4=123)			#这里的字典是{"key4":123}
# dict_test.update({key4: 1234})
# print(dict_test)


#1
'''
小蓝正在玩拼图游戏，他有7385137888721个2x2的方块和 10470245 个1x1的方块，
他需要从中挑出一些来拼出一个正方形，比如用3个2x2和4个1x1的方块可以拼出一个4x4的正方形，
用9个2x2的方块可以拼出一个6x6的正方形，请问小蓝能拼成的最大的正方形的边长为多少。'''
# # print(7385137888721*2)
# # print(14770275777442+10470245)
# total1 = 14770286247687
# print(len(str(total1)))
# print(1000000*1000000 > 14770286247687)
# for number in range(1000000,10000000):
#     while number*number < 14770286247687 and (number+1)*(number+1) > 14770286247687:
#         zhengfangxing = number
#         print(number)
#         break
# print(zhengfangxing)
# #2
# # print(10470245/4)
# # print(7385137888721+2617561)
# # total2 = 7385140506282


'''
小蓝想要构造出一个长度为T0000 的数字字符串，有以下要求:
1)小蓝不喜欢数字0，所以数字字符串中不可以出现 0:
2)小蓝喜欢数字3和7，所以数字字符串中必须要有3和7这两个数字。
请问满足题意的数字字符串有多少个?这个数字会很大，你只需要输出其
对 10的9次方+7 取余后的结果。
'''

num_str = ''
for num in range(1,10001):
    num_str = num_str + '9'
    while len(num_str) == 10000:
        print(num_str)
        print(type(num_str))
        break
num = int(num_str)
print(num)
print(type(num))