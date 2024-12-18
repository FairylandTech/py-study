# s = "  jkfjj字  "
# s1 = "    aq qa qf 天 字符串 "
# s2 = "好好学习,天天向上"
# 1. 去掉字符串中所有的空格
# 2. 将字母全部转换为大写和小写
# 3. 计算字符串长度
# 4. 判断一个字符串是否是另一个字符串的子串
# 5. 字符串中汉字的个数
# 6. 找出所有"字"的位置
# 7. 生成长度为10无数字的全字母的字符串
# 9. 生成长度为10有数字的全字母的字符串
# 10. 根据标点符号对字符串进行分行
# 11. 字符串翻转


# #   1. 去掉字符串中所有的空格   ---------------------------------------------------------
# s = "  jkfjj字  "
# s1 = "    aq qa qf 天 字符串 "
# s2 = "好好学习,天天向上"
# # d = s+s1
# # print(d)
# ss = s.split(' ')
# print(ss)
# ss1 = s1.split(' ')
# print(ss1)
#
# sc= ''
# sc1 = ''
#
# for i in ss:
#     if i not in  ' ':
#         s = sc + i
#         print(s)
#         print(type(s))
#
# for i in ss1:
#     if i not in  ' ':
#         sc1 = sc1 + i
#         print(sc1)
#         print(type(sc1))
#
# # for i in ss:
# #     if i:
# #         s = sc + i
# #
# #     print(s)
#
#
# # for i in ss:
# #     if i == ' ':
# #         pass
# #     else:
# #         s = sc + i
# #         print(s)


# #     2. 将字母全部转换为大写和小写------------------------------------------------------
# s = "jkfjj字"
# s1 = "aqqaqf天字符串"
# s2 = "好好学习,天天向上"
#
# s = s.upper()
# print(s)
# s = s.lower()
# print(s)
#
# s1 = s1.upper()
# print(s1)
# s1 = s1.lower()
# print(s1)


## 3. 计算字符串长度-------------------------------------------------------------------
# print(len(s))
# print(len(s1))
# print(len(s2))


# 4. 判断一个字符串是否是另一个字符串的子串----------------------------------------------
# s = "jkfjj字"
# s1 = "aqqaqf天字符串 "
# s2 = "好好学习,天天向上"
# # print(s in s1)
# l = [s,s1,s2]
# for i in l:
#     l.remove(i)
#     l1 = l
#     # print(l1)
#     for j in l1:
#         print(i in j)
#
# q= sdf
# g = asdfg
# e = sd

# 5. 字符串中汉字的个数--------------------------------------------------------------------
# import string
# # print(string.ascii_letters)
# # print(string.ascii_lowercase)
# # print(string.ascii_uppercase)
# # print(string.digits)
# s = "jkfjj字"
# s1 = "aqqaqf天字符串 "
# s2 = "好好学习,天天向上"
# l = [s,s1,s2]
# english = string.ascii_letters
# numbe = string.digits
# #问题，把标点符号与空格也算进去了
# for i in l:
#     chinese = 0
#     for j in i:
#         if j not in english and j not in numbe:
#             chinese +=1
#     print(chinese)

# # 6. 找出所有"字"的位置---------------------------------------------------------------
# s = "jkfjj字"
# s1 = "aqqaqf天字符串 "
# s2 = "好好学习,天天向上"
# l = [s,s1,s2]
#
# for i in l:
#     postion = 0
#     for j in i:
#         if j == '字':
#             print(postion)
#         else:
#             postion = postion + 1

# 7. 生成长度为10无数字的全字母的字符串-----------------------------------------------------------
import string
import random

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)

english = string.ascii_letters
# print(type(english))
eng_str = ''
# print(r)

# #1  问题，按顺序取值了，不是随机的
# for i in range(0,52):
#     if len(eng_str) >=10:
#         print(eng_str)
#     else:
#         eng_str = eng_str + english[i]


# #报错
# for i in random.randint(0, 51):
#     if len(eng_str) >= 10:
#         print(eng_str)
#     else:
#         eng_str = eng_str + english[i]

# # 无结果
# r = random.randint(0, 51)
# for i in range(r,r+1):
#     if len(eng_str) >= 10:
#         print(eng_str)
#     else:
#         eng_str = eng_str + english[i]

# 成功----------------------------------------------------
# for i in english:
#     r = random.randint(0, 51)
#     if len(eng_str) >= 10:
#         print(eng_str)
#     else:
#         eng_str = eng_str + english[r]

# # #问题，while 设置为10无任何输出结果，加上for循环无任何输出结果，设为11陷入死循环(解决)
# while len(eng_str) <= 10:
#     r = random.randint(0, 51)
#     # for i in range(r,r+1):
#     if len(eng_str) >= 10:
#         print(eng_str)
#         break
#     else:
#         eng_str = eng_str + english[r]


# 9. 生成长度为10有数字的全字母的字符串
import string
import random

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)

english = string.ascii_letters
num = string.digits

# #  比较复杂，不好实现，字母和数字的个数，与所在位置全随机，
# english_pl = random.randint(1,9)
# num_pl = 10-english_pl
# # print(english_pl)
# # print(type(english_pl))
# # print(num_pl)
# # print(type(num_pl))
# eng_num_str = ''
#
# for i in english:
#     r = random.randint(0, 51)
#     if len(eng_num_str) >= 10:
#         print(eng_num_str)
#     else:
#         eng_num_str = eng_num_str + english[r]

# #  成功---------------------------------------------------
# eng_num = english+num
# eng_num_str = ''
# # print(eng_num)
# for i in eng_num:
#     r = random.randint(0, 61)
#     if len(eng_num_str) >= 10:
#         print(eng_num_str)
#     else:
#         eng_num_str = eng_num_str + eng_num[r]

# 10. 根据标点符号对字符串进行分行
s = "jkfjj字"
s1 = "aqqaqf天字符串 "
s2 = "好好学习,天天向上"
s3 = '''i哦和，
阿斗'''
#
# l = [s,s1,s2]
#
# for i in l:
#     postion = 0
#     for j in i:
#         if j == ',':
#
#         else:
#             postion = postion + 1
# print(s3)
# print(type(s3))
q = s2.split(',')
for i in range(0,len(q)-1):
    s4 = q[i]
    if i < len(q):
        i = i + 1
        s4= s4+'\n'+q[i]

    print(s4)

    # print(i)
    # print(type(i))

# print(q)
# print(type(q))

# 11. 字符串翻转
# print(s[::-1])
# print(s1[::-1])
# print(s2[::-1])






list_name = ['田春和', '柳广', '橘井', '王怡']
list_name.append('季朝阳')  # 添加数据到最后一位
list_name.insert(2, '司离人')  # 根据下标插入新数据
# list_name.insert(2, '司离人','季朝阳') # 报错 一个萝卜一个坑
# list_name.extend('季朝阳') # 打散数据添加到最后一位
# list_name.extend(('季朝阳', '花花'))  # 打散数据添加到最后一位
print(list_name)