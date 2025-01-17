import random

# print(random.random())   # (0, 1)

# print(random.uniform(5, 9))  # 随机小数

# print(random.randint(3, 8))  # 随机整数. 能够取到边界


# lst = ["张无忌", '周杰伦', "潘玮柏", "赵四"]
#
# print(random.choice(lst))  # 随机的选择一个

# lst = ["屠龙刀", "倚天剑", "500金币", "青龙偃月刀", "溜溜球"]
# # 每次随机爆出2个装备
# print(random.sample(lst, 2))


# 练习题: 随机生成四位验证码
# 四位验证码. 一个一个的生成
# 可能会有数字, 可能会有大写字母, 可能会有小写字母


def rand_num():
    return str(random.randint(0, 9))

def rand_upper():
    return chr(random.randint(65, 90))

def rand_lower():
    return chr(random.randint(97, 122))


# 随机验证码,默认是4位
def rand_verify_code(n=4):
    lst = []  # ['A', '4', 'b', 'A']
    for i in range(n):
        which = random.randint(1, 3)
        if which == 1:  # 随机数字
            s = rand_num()
        elif which == 2:  # 随机大写字母
            s = rand_upper()
        elif which == 3:
            s = rand_lower()
        lst.append(s)
    return "".join(lst)

print(rand_verify_code(6))






