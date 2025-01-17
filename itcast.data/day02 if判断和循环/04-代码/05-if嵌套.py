# 假设 money 大于等于2 可以上车
money = int(input('请输入你拥有的零钱:'))
# ctrl x 剪切  ctrl v  粘贴

# 1. 有钱可以上车
if money >= 2:
    print('我上车了')
    # 假设 seat 大于等于1,就可以坐
    seat = int(input('车上的空位个数:'))
    # 3. 有空座位,可以坐
    if seat >= 1:
        print('有座位坐')
    else:
        # 4. 没有空座位,就站着
        print('没有座位,只能站着')
else:
    # 2. 没钱不能上车,走路
    print('没钱,我只能走路')


