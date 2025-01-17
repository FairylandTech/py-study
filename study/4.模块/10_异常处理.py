# try...except来处理异常
# try:
#     print(1/0)
# except:
#     print("程序好像出错了, 请联系管理员")

"""
try:
    try-代码
except 错误1 as 变量1:
    except1代码
except 错误2 as 变量2:
    except2代码
except Exception as e:
    最终
....
finally:
    收尾
"""
# try:
#     # print(1/0)
#     # open("hehehehehehe", mode="r").read()
#     lst = []
#     # lst.__iter__().__next__()
# except ZeroDivisionError as z:
#     print("除数为0")
# except FileNotFoundError as f:
#     print("文件不存在")
# except Exception as e:  # 万能的错误接收
#     print("系统错误")
#
# finally:  # 不论是否出错, 都要执行finally
#     print("收尾")


# 程序是可以自己抛出异常的.
def func(a, b):  # 计算两个int类型的数字的和
    if type(a) == int and type(b) == int:
        return a + b
    else:
        # 抛出异常. 谁调用的该函数, 谁接收该异常
        raise Exception("你给我的不是int类型. func函数无法进行计算")


func("呵呵", 1)


# 1. 处理异常, try...except
# 2. 抛出异常, raise



