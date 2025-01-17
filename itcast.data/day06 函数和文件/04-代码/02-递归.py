def get_age(num):
    """
    求第 num 个人的年龄,每相邻的两个人的年龄差两岁, 已知第一个人的年龄是 18岁
    :param num:
    :return:
    """
    if num == 1:
        return 18
    # 求第 num个人的年龄,只需要num-1 这个人的年龄 + 2
    age = get_age(num-1) + 2
    return age


print(get_age(4))