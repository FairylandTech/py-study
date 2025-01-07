# lst = [11, 25, 46, 78, 99, 265]
# n = int(input(">>>"))
# for item in lst:
#     if item == n:
#         print('存在')
#         break
# else:
#     print('不存在')


# lst = [11, 25, 46, 78, 99, 265]
#
# n = int(input(">>>:"))
# left = 0
# right = len(lst) - 1  # 最大索引号

# while left <= right:
#     mid = (left + right) // 2  # 计算中间位置的索引号
#     if n > lst[mid]:
#         left = mid + 1
#     elif n < lst[mid]:
#         right = mid - 1
#     else:
#         print("找到了数据, 位置", mid)
#         break
# else:
#     print('没找到')


# 递归版本的算法
lst = [11, 25, 46, 78, 99, 265]

n = int(input(">>>:"))
left = 0
right = len(lst) - 1  # 最大索引号

def find(lst, n, left, right):
    if left > right:
        print("没找到")
        return
    mid = (left + right)//2
    if n > lst[mid]:
        left = mid + 1
    elif n < lst[mid]:
        right = mid - 1
    else:
        print("找到了, 索引位置", mid)
        return
    find(lst, n, left, right)  # 进入递归

find(lst, n, left, right)





