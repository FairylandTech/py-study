# 无限喷人
# while True:
#     content = input("请输入你要发送给打野的话(Q退出):")
#     if content == "Q":
#         break  # break可以结束这个循环
#     print("我想对打野说:" + content)


while True:
    content = input("请输入你要发送给打野的话(Q退出):")
    if content == "Q":
        continue  # 结束当前本次循环, 继续执行下一次循环
    print("我想对打野说:" + content)

