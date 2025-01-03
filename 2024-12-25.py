# '''1. 数据类型转换：编写一个函数，将输入的字符串转换为浮点数。如果转换失败，返回None。
# 例如，输入 "3.14" 返回 3.14，输入 "abc" 返回 None。'''
from webbrowser import Error

#  不标准
# a = input('请输入：')
#
# def s_f(a):
#     try:
#         return float(a)
#
#     except error as e:
#         # raise None
#         return None
# print(s_f(a))



# '''2. 找出列表中的最大值：编写一个函数，接受一个包含整数的列表，返回列表中的最大值。
# 你不能使用内置的 max 函数。'''
#
# num_list = [1,5,9,15,6,4,3,2]
# def max_num(l):
#     l.sort(reverse=True)
#     # print(l)
#     return l[0]
# print(max_num(num_list))

# '''3. 判断闰年：编写一个函数，判断给定的年份是否为闰年。
# 闰年判断规则：能被4整除但不能被100整除，或者能被400整除。'''
#
# years = input('请输入年份：')
# def rwen(year):
#     yea = int(year)
#     if yea%4 == 0 and yea%100 !=0 and yea%400 !=0:
#         print('这是闰年')
#     else:
#         print('不是闰年')
# rwen(years)

'''4. 统计字符串中的元音字母：编写一个函数，统计并返回给定字符串中的元音字母（a, e, i, o, u）个数。'''
# yuan = 'aeiou'
# zimu = input('请输入内容：')
# def geshu(zm):
#     for i in yuan:
#         ge = 0
#         # for j in zm:
#         if i in zm:
#             ge = ge + zm.count(i)
#             print(f'{i}在{zm}里有{ge}个')
# geshu(zimu)

# '''5. FizzBuzz：编写一个函数，打印从1到100的数字。
# 如果数字是3的倍数，打印"Fizz"；
# 如果是5的倍数，打印"Buzz"；
# 如果既是3的倍数又是5的倍数，打印"FizzBuzz"。'''
#
# def dayin():
#     for i in range(1,101):
#         if i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
#         elif i % 3 == 0:
#             print('Buzz')
#         elif i % 5 == 0:
#             print('Fizz')
#         else:
#             print(i)
# dayin()

'''6. 平方数列表：使用列表推导式创建一个包含前20个整数的平方的列表。'''



'''7. 字典值的平方和：编写一个函数，接受一个字典，并返回字典中所有值的平方和。
假设字典中的值都是整数。例如，输入 {"a": 1, "b": 2, "c": 3}，返回 1^2 + 2^2 + 3^2 = 14。'''

'''8. 统计列表中元素的频率：编写一个函数，统计并返回列表中每个元素出现的频率。
返回一个字典，其中键是元素，值是元素出现的次数。'''

'''9. 查找缺失的数字：编写一个函数，接受一个包含1到100中缺失一个数字的列表，找出并返回这个缺失的数字。
例如，输入 [1, 2, 3, ..., 99, 100] 缺失了 45，函数应返回 45。'''

'''10. 判断字符串回文：编写一个函数，判断给定的字符串是否为回文。
回文是指正读和反读都相同的字符串，例如 "radar"、"level"。'''