# 1. 无参无返回值
def func1():
    print('hello')


(lambda: print('hello lambda'))()
func1()
f1 = lambda: print('hello lambda')
f1()


# 2. 无参有返回值
def func2():
    return 1 + 2


f2 = lambda: 1 + 2
print(f2())


# 3. 有参无返回值
def func3(name):
    print(name)


f3 = lambda name: print(name)
f3('hwllo')


# 4. 有参有返回值
def func4(*args):
    return args


f4 = lambda *args: args
print(f4(1, 2, 3, 4, 5))