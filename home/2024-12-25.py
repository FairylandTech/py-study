# '''1. 数据类型转换：编写一个函数，将输入的字符串转换为浮点数。如果转换失败，返回None。
# 例如，输入 "3.14" 返回 3.14，输入 "abc" 返回 None。'''

#  不标准
# a = input('请输入：')
def s_f(a):
    try:
        return float(a)

    except Exception as e:
        # raise None
        return None
# print(s_f(a))

#  标准

# str1 = input('请输入：')
def str2float():
    pass
def str_convert_float(string):
    try:
        return float(string)
    except Exception  as e:
        return None
# print(str_convert_float(str1))



# '''2. 找出列表中的最大值：编写一个函数，接受一个包含整数的列表，返回列表中的最大值。
# 你不能使用内置的 max 函数。'''

#  标准
num_list = [1,5,9,15,6,4,3,2]
def max_num(l):
    l.sort(reverse=True)
    # print(l)
    return l[0]
# print(max_num(num_list))


# '''3. 判断闰年：编写一个函数，判断给定的年份是否为闰年。
# 闰年判断规则：能被4整除但不能被100整除，或者能被400整除。'''

#  不标准
# years = input('请输入年份：')
def rwen(year):
    yea = int(year)
    if yea%4 == 0 and yea%100 !=0 or yea%400 ==0:
        print('这是闰年')
    else:
        print('不是闰年')
# rwen(years)

#  标准
# year = input('请输入年份：')
def judge_leap_year(years):
    years = int(years)
    if years%4 == 0 and years%100 !=0 or years%400 ==0:
        print('这是闰年')
    else:
        print('不是闰年')
# judge_leap_year(year)

'''4. 统计字符串中的元音字母：编写一个函数，统计并返回给定字符串中的元音字母（a, e, i, o, u）个数。'''
#  不标准
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

def geshu2(zm):
    yuan = 'aeiou'
    count = 0
    for i in zm:
        if i in yuan:
            count += 1
    return count

#  标准
vowel = 'aeiou'
# str_words = input('请输入内容：')
def count_vowel(words):
    for i in vowel:
        ge = 0
        # for j in str_words:
        if i in words:
            ge = ge + words.count(i)
            print(f'{i}在{words}里有{ge}个')
# count_vowel(str_words)

# print(geshu2("aeiouaeiouaeiouaeiouaeiouaeiou"))

# '''5. FizzBuzz：编写一个函数，打印从1到100的数字。
# 如果数字是3的倍数，打印"Fizz"；
# 如果是5的倍数，打印"Buzz"；
# 如果既是3的倍数又是5的倍数，打印"FizzBuzz"。'''

#  不标准
def dayin():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Buzz')
        elif i % 5 == 0:
            print('Fizz')
        else:
            print(i)
# dayin()

#  标准
def print_special_number():
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Buzz')
        elif number % 5 == 0:
            print('Fizz')
        else:
            print(number)
# print_special_number()

# '''6. 平方数列表：使用列表推导式创建一个包含前20个整数的平方的列表。'''

#  不标准
a = []
a.append([i**2 for i in range(1,21)])
a = [i ** 2 for i in range(1, 21)]
# print(a)

#  标准
square_list = []
square_list.append([square_number ** 2 for square_number in range(1, 21)])
# print(square_list)

# '''7. 字典值的平方和：编写一个函数，接受一个字典，并返回字典中所有值的平方和。
# 假设字典中的值都是整数。例如，输入 {"a": 1, "b": 2, "c": 3}，返回 1^2 + 2^2 + 3^2 = 14。'''
#
dicta = {"a": 1, "b": 2, "c": 3}
#  不标准
def pf(kv):
    he = 0
    pingfang = ''
    for i in kv:
        num = dicta.get(i)
        he += num**2
        pingfang += f'{num}^2+'

    pingfang = pingfang[0:len(pingfang)-1]
    print(f'{pingfang}={he}')
# pf(dicta)

def pf2(dicts):
    sum_num = 0
    content = ""
    for value in dicts.values():
        sum_num += value ** 2
        content += f"{value}^2+"
    return f"{content[:-1]}={sum_num}"
# print(pf2(dicta))

#  标准
def add_square(number_dict):
    sum = 0
    suqare = ''
    for number in number_dict:
        num = dicta.get(number)
        sum += num**2
        suqare += f'{num}^2+'

    suqare = suqare[0:len(suqare)-1]
    print(f'{suqare}={sum}')
# add_square(dicta)

# '''8. 统计列表中元素的频率：编写一个函数，统计并返回列表中每个元素出现的频率。
# 返回一个字典，其中键是元素，值是元素出现的次数。'''
#


list1 = ['1', '2', '3', '1', '2']


from collections import Counter
# print(dict(Counter(list1)))


def pl(li):
    list2 = []
    for i in li:
        list2.append(i)

    list2 = set(list2)
    dicta = {}
    for i in list2:
        dicta[f"{i}"] = li.count(i)
    return dicta
    # print(list2)
        # ci = li.count(i)
        # print(ci)
# print(pl(list1))


def count_frequency(count_dict):
    frequency_list = []
    for vulue in count_dict:
        frequency_list.append(vulue)

    frequency_list = set(frequency_list)
    none_dict = {}
    for vulue in frequency_list:
        none_dict[f"{vulue}"] = count_dict.count(vulue)
    return none_dict
    # print(list2)
        # ci = li.count(i)
        # print(ci)
# print(count_frequency(list1))

# '''9. 查找缺失的数字：编写一个函数，接受一个包含1到100中缺失一个数字的列表，找出并返回这个缺失的数字。
# 例如，输入 [1, 2, 3, ..., 99, 100] 缺失了 45，函数应返回 45。'''
# #存在问题    ------------------------------------------------------------------------------------------
list1 = []
for number in range(1, 101):
    list1.append(number)
list1.pop(44)
# list1.pop(44)


def que1(list1):
    return  ", ".join([str(i) for i in range(1,101) if i not in list1])
# print(que1(list1))


def que(li):
    q = None
    for i in range(1, 101):
        if i not in li:
            print('缺失的数字是：',i)
            q = i
    return q


print(que(list1))


def find_missing_number(number_list):
    missing = None
    for number in range(1, 101):
        if number not in number_list:
            print('缺失的数字是：',number)
            missing = number
    return missing


print(find_missing_number(list1))


# '''10. 判断字符串回文：编写一个函数，判断给定的字符串是否为回文。
# 回文是指正读和反读都相同的字符串，例如 "radar"、"level"。'''

str1 = 'radar'
str2 = 'level'
str3 = 'adasas'
def hui(wen):
    if wen == wen[::-1]:
        print('这是回文')
    else:
        print('这不是回文')
# hui(str1)
# hui(str2)
# hui(str3)


def judge_palindrome(palindrome):
    if palindrome == palindrome[::-1]:
        print('这是回文')
    else:
        print('这不是回文')
judge_palindrome(str1)
judge_palindrome(str2)
judge_palindrome(str3)
