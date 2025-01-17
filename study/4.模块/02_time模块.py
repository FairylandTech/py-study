import time

# # sleep()  可以暂停执行一段时间
# print("你好")
# time.sleep(3)
# print("你才好呢")


# 可以控制程序执行的频率
# while True:
#     print("抓取百度的信息")
#     time.sleep(1)


# print(time.time())   # 1583999077 时间戳  数字类型的时间
# 123

# 可以计算时间差

start = time.time()
for i in range(1000000):
    print(i)
end = time.time()
print(end - start)   # 计算时间差


