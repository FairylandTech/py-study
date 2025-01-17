# for c in "你好":
#     print(c)
#
# for i in 123:   # int类型不可以被迭代
#     print(i)

# print(dir(str))   # 有__iter__
# print(dir(list))  # 也有__iter__
# print(dir(dict))  # 也有__iter__
# print(dir(int))   # int没有__iter__
# print("__iter__" in dir(bool))  # bool也没有__iter__


# # iterable 可迭代的
# # 所有的可迭代对象内部都含有一个__iter__的功能
# lst = ["你好", "你不好", "你很好"]
# it = lst.__iter__()  # iterator 迭代器
# print(dir(it))
# ret = it.__next__()  # 你好
# print(ret)
# ret = it.__next__()  # 你不好
# print(ret)
# ret = it.__next__()  # 你很好
# print(ret)
# ret = it.__next__()   # 这里会报错  StopIteration
# print(ret)

# 使用步骤:
#   1. 通过__iter__拿到可迭代对象中的迭代器
#   2. 用迭代器执行__next__拿到元素.
#   3. 重复第二步. 反复执行. 直到最后出现了StopIteration结束

s = {"你好", "哒哒哒哒", "嘚吧嘚"}
# it = s.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# 坑
#   1.想让迭代器重头拿数据. 需要重新拿到迭代器
# it = s.__iter__()
# print(it.__next__())
# print(it.__next__())

# # 2. 这里不适合使用数学上的等价代换
# print(s.__iter__().__next__())
# print(s.__iter__().__next__())
# print(s.__iter__().__next__())

# # 还可以使用iter() 来获取迭代器
# lst = [11,22,33]
# it = iter(lst)   # iter = __iter__
# print(next(it))  # next = __next__
# print(next(it))
# print(next(it))


lst = []
it = lst.__iter__()


print(dir(lst))   # 列表不是迭代器.
print(dir(it))    # 迭代器本身是一个可迭代对象. 迭代器可以使用for循环
