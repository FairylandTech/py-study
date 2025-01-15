# coding=UTF-8

import time

"""
1. 写装饰器. 控制函数被调用的频率. 要求: 5秒钟执行一次. 少于5秒钟直接打印警告信息.
"""


def alt_time(seconds):
    def outer(func):
        last_called = [0]
        def inner(*args, **kwargs):
            now_timestamp = time.time()
            if now_timestamp - last_called[0] < seconds:
                print("Warring ......")
            else:
                result = func(*args, **kwargs)
                last_called[0] = int(time.time())
                return result


        return inner

    return outer


@alt_time(5)
def main():
    print("执行main方法")

if __name__ == '__main__':
    main()
    time.sleep(2)
    main()
    time.sleep(5)
    main()
