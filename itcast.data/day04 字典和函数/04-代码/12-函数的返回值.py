# 函数想要返回一个数据值,给调用的地方,需要使用关键字 return
# return 关键字的作用: ①, 将return 后边的数据值进行返回 ②,程序代码遇到return, 会终止(结束)执行
# 注意点: return 关键字必须写在函数中


def add(a, b):
    c = a + b
    # 想要将求和的结果 c, 返回,即函数外部使用求和的结果, 不在函数内部打印结果
    return c
    print(f'求和的结果是{c}')   # 函数遇到return就结束了,不会执行return之后的代码


result = add(100, 200)
print(f'函数外部获得了求和的结果{result}')

print(add(10, 30))

