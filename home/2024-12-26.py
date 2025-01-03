'''
1.   求和数字字符串：编写一个函数，接受一个包含数字字符串的列表，返回这些字符串表示的数字之和。
例如，输入 ["1", "2", "3.5"]，返回 6.5。
'''


number_list = ["1", "2", "3.5", 'hello']

def sum_str(num_list):
    sum = 0
    for number in num_list:
        number = float(number)
        sum += number
    return sum


# print(sum_str(number_list))


'''
2.   生成斐波那契数列：编写一个生成斐波那契数列前n个数的函数，使用生成器实现。斐波那契数列是指前两项为1，从第三项起，每一项是前两项之和。
'''


# 1 1 2 3 5 8 13 21 34
def produce_n_Fibonacci_sequence(production_n_place):
    Fibonacci_sequence = [1,1]
    if production_n_place == 1:
        Fibonacci_sequence = [1]
    elif production_n_place == 2:
        Fibonacci_sequence = [1,1]
    else:
        len_num = 2
        while len_num <= production_n_place:
            next_num = Fibonacci_sequence[-1] + Fibonacci_sequence[-2]
            Fibonacci_sequence.append(next_num)
            len_num += 1
            if len_num == production_n_place:
                break
    return Fibonacci_sequence


# print(produce_n_Fibonacci_sequence(9))


'''
3.   统计文件字符频率：编写一个函数，读取一个文本文件，并统计文件中每个字符出现的频率。返回一个字典，其中键是字符，值是字符出现的次数。
'''


# with open(r"C:\Users\20560\Desktop\pycharm   project\py-study\py-study\文本.txt", "r") as file:
with open(r"../文本.txt", "r") as file:
    data = file.read()
    # print(data)
    # print(type(data))
from collections import Counter
count = dict(Counter(data))
# print(count)


'''
4.   合并两个有序列表：编写一个函数，合并两个有序的整数列表，并返回一个有序的新列表。不能使用内置的排序函数。
'''


int_list1 = [2,7,5,]
int_list2 = [1,8,3,]
# print(len(int_list1))
def merge_in_order(int_list1, int_list2):
    merged_list = []

    while int_list1 != [] and int_list2 != []:
        min1 = min(int_list1)
        min2 = min(int_list2)
        if min1 > min2:
            merged_list.append(min2)
            int_list2.remove(min2)
        elif min2 > min1:
            merged_list.append(min1)
            int_list1.remove(min1)

    if int_list1 == []:
        num = len(int_list2)
        while num >= 1:
            merged_list.append(min(int_list2))
            int_list2.remove(min(int_list2))
            num -= 1
            if num == 0:
                break
    elif int_list2 == []:
        num = len(int_list1)
        while num >= 1:
            merged_list.append(min(int_list1))
            int_list1.remove(min(int_list1))
            num -= 1
            if num == 0:
                break
    return merged_list


# print(merge_in_order(int_list1, int_list2))


'''
5.   实现自定义Map函数：编写一个函数，接受一个函数和一个列表作为参数，实现与内置map函数类似的功能，
即对列表中的每个元素应用给定的函数，并返回一个新的列表。
'''


number_list = ["1", "2", "3.5"]
def sum_str(num_list):
    sum = 0
    for number in num_list:
        number = float(number)
        sum += number
    return sum


# a = sum_str(number_list)
# print(a)


def custom_map(func,a_list):
    return func(a_list)


# print(custom_Map(sum_str, number_list))


'''
6.   矩阵转置：编写一个函数，接受一个n行m列的矩阵，返回其转置矩阵。
转置矩阵是指行和列互换的新矩阵。
'''


matrix = [
    [1,3,4,5],
    [2,8,1,9],
    [5,2,4,7],
    [1,2,3,4]
]

def trans():
    new_list = []
    for row in zip(*matrix):
        new_list.append(list(row))
    return new_list


# print(trans())
# print(len(matrix[2]))
# print(len(matrix))
#
# transponsed = [[],[],[],[]]
# transponsed[2].append(matrix[1][2])
# print(transponsed)


def transponsed_matrix(matrix):
    #行
    n = len(matrix)
    #列
    m = len(matrix[0])
    transponsed = []
    #生成行
    for line in range(1,m+1):
        transponsed.append([])
    print(transponsed)

    #获取每行数据
    for row_num in matrix:
        #获取行索引
        row_index = matrix.index(row_num)
        # print(row_index)
        # print(type(row_index))
        #读取每行的内容，放到列里
        for line_num in row_num:
            #获取一行每个元素的索引
            line_index = row_num.index(line_num)
            # print(line_index)
            # print(type(line_index))
            # transponsed[line_index].append(matrix[row_index][line_index])
            transponsed[line_index].append(row_num[line_index])
    print(transponsed)
# transponsed_matrix(matrix)


'''
7.   找出缺失的字母：编写一个函数，接受一个包含所有小写字母但随机缺失一个字母的字符串，找出并返回缺失的字母。
例如，输入 "abcdefghijklmnopqrstuvwxy"，返回 "z"。
'''


lack_str = "abcdefghijklmnopqrstuvwxy"

def find_missing_case(lack_str):
    import string
    lowercase = string.ascii_lowercase
    lack_return = None
    for lack in lowercase:
        if lack not in lack_str:
            lack_return = lack
    return lack_return


# print(find_missing_case(lack_str))

'''
8.   统计词频：编写一个函数，读取一个文本文件，统计文件中每个单词出现的频率。
返回一个字典，其中键是单词，值是单词出现的次数。
'''


# with open(r"C:\Users\20560\Desktop\pycharm   project\py-study\py-study\文本.txt", "r") as file:
# with open(r"../文本.txt", "r") as file:
#     data = file.read()
#     print(data)
#     print(type(data))
#
#     data = data.split("\n")
#     print(data)
#     data = ''.join(i for i in data)
#     print(repr(data))
#     frequency_counter = {}
#     set_word = set()
#     for word in data.split(" "):
#         # print(type(word))
#         set_word.add(word)
#     print(set_word)
#     dict_key = list(set_word)
#     for word in dict_key:
#         frequency_counter[word] = data.count(word)
#     print(frequency_counter)


# from collections import Counter
# test = Counter(data)
# print(test)
# print(type(test))
# count = dict(Counter(data))
# print(count)


'''
9.   括号匹配：编写一个函数，判断一个字符串中的括号是否匹配。括号包括()、[]、{}，匹配是指每个左括号都有相应的右括号并且顺序正确
'''

str_bracket = "(aas),[vd],{ofd},{"
def bracket_matching(bracket):
    left_small = bracket.count('(')
    # print(left_small)
    right_small = bracket.count(')')
    if left_small == right_small:
        print('()是匹配的')
    elif left_small > right_small:
        difference = left_small - right_small
        print(f' ’(‘ 缺少{difference}个匹配的 ’)‘')
    elif right_small > left_small:
        difference = left_small - right_small
        print(f' ’)‘ 缺少{difference}个匹配的 ’(‘')

    left_middle = bracket.count('[')
    right_middle = bracket.count(']')
    print(left_small)
    print(right_small)

    if left_middle == right_middle:
        print('[]是匹配的')
    elif left_middle > right_middle:
        difference = left_small - right_small
        print(left_small)
        print(right_small)
        print(f' ’[‘ 缺少{difference}个匹配的 ’]‘')
    elif right_middle > left_middle:
        difference = left_small - right_small
        print(f' ’]‘ 缺少{difference}个匹配的 ’[‘')

    left_big = bracket.count('{')
    right_big = bracket.count('}')

    if left_big == right_big:
        print('{}是匹配的')
    elif left_big > right_big:
        difference = left_small - right_small
        print(' ’{‘ 缺少%d个匹配的 ’}‘'%(difference))
    elif right_big > left_big:
        difference = left_small - right_small
        print(' ’}‘ 缺少%d个匹配的 ’{‘'%(difference))


# bracket_matching(str_bracket)


'''
10.   解析JSON字符串：编写一个函数，接受一个JSON格式的字符串，解析并返回对应的Python数据结构（如字典或列表）。
如果解析失败，返回
'''

s_t_r = {'姓名':'法外狂徒'}
json_str = "{'姓名':'法外狂徒','身高':181,'体重'：188}"
print(json_str)
print(type(json_str))

# json_str = list(json_str)
# print(json_str)
# print(type(json_str))

json_str = list(json_str)
print(json_str)
print(type(json_str))


def analysis_json_str(json_str):
    pass