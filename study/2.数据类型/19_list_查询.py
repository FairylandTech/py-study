# lst = ["周杰伦", "林俊杰", "吴克群", "潘玮柏", "呵呵"]

# for item in lst:
#     print(item)

# 想看一下索引和元素
# # while
# i = 0
# while i < len(lst):
#     item = lst[i]  # 元素
#     print(item)
#     print(i)  # 索引
#     i += 1

# 如何让for循环去数数
# range() 给for循环搭配使用的.

# # range(n) 从0数到n-1,  [0, n)
# for i in range(10):
#     print(i)

# # range(m, n)  从m数到n-1, [m, n)
# for i in range(5, 10):  # [5, 9)
#     print(i)

# # range(m, n, s)  # 和切片逻辑是一致的.
# for i in range(1, 10, 2):
#     print(i)

# i = 0
# while i < 10:
#     print(i)
#     i+=1


# # 使用for循环, 拿到索引和元素
# for i in range(len(lst)):
#     print(i)
#     print(lst[i])


# # 在列表中找到姓王的. 然后把姓王的名字全部改成"帅哥"
# lst = ["王重阳", "谢广坤", "刘能", "王大拿"]
# # 必须要有索引, 还要有元素
# for i in range(len(lst)):
#     item = lst[i]
#     if item.startswith("王"):  # 判断是否姓王
#         lst[i] = "帅哥" # 修改
# print(lst)




