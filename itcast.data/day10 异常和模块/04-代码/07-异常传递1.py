print('其他的功能代码.....')
num = input('请输入数字:')
try:
    try:
        a = int(num)  # ValueError
    except ZeroDivisionError:
        print('发生异常')
    finally:
        print('我都执行了....')

    num = 10 / a
    print(f'计算的结果<<{num}>>')
except Exception as e:
    print(e)


print('其他的功能代码.....')