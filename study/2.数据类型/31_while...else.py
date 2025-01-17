# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:  # 条件不成立的时候. 默认执行这里
#     print("OK!")


# i = 0
# while i < 10:
#     if i == 7:
#         break   # 结束这个循环
#     print(i)
#     i += 1
# else:  # 条件不成立的时候. 默认执行这里
#     print("OK!")
#
# # 如果执行到break 就不执行else
# # 如果从头到尾都没有执行break, 最后一定执行else


# 练习: 让用户随便输入一个数字, 判断这个数组, 是否是质数
n = int(input("请输入一个数字:").strip())   # 7
# 数学: 质数是: 只能被1和自身整除的数
i = 2
while i < n:  # 2, n-1
    if n % i == 0:  # 整除, 不是质数
        print("不是质数")
        break  # 结束
    i += 1
else:
    print("是质数")




