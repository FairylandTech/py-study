"""
    函数: 对功能或者动作的封装
    定义:
        def 函数名(形参):
            函数体
            return

        函数名(实参)

        形参:
            1. 位置参数
            2. 默认值参数
            3. 动态传参: *, ** 可以接受位置参数或者关键字参数的动态传参
            顺序: 位置参数 > *args > 默认值 > **kwargs

        实参:
            1. 位置参数
            2. 关键字参数
            3. 混合参数 顺序(先位置, 后关键字)
            *和**还表示把列表或者元组打散成位置参数或者关键字参数进行传递

        返回值:
            return 结束函数的执行
            一个返回值  return 值
            多个返回值  return 值1, 值2....

        globals()
        locals()

        global和nonlocal
            global可以把全局变量引入到局部
            nonlocal可以把局部外层变量引入到内层函数中使用

        闭包: 内层函数使用了外层函数中的变量
            1. 保护变量不被修改
            2. 让变量常驻内存

        通用装饰器:
            def wrapper(fn):
                def inner(*args, **kwargs);
                    ret = fn(*args, **kwargs)
                    retrun ret
                return inner

            @wrapper  # target = wrapper(target)
            def target():
                pass

            target() # 实际上执行的是inner函数

        迭代器:
            只能下一个下一个.
            统一了所有需要遍历的数据类型的遍历方式

        生成器:
            本质就是迭代器
            1. 通过生成器函数创建
                yield
                特点: 在执行该函数的时候. 默认是创建一个新的生成器. 此时不会执行你的函数
                gen.__next__()  可以让函数分段执行, 每次执行到下一个yield
                gen.send(值)  可以让函数分段执行, 每次执行到下一个yield 可以给上一个yield位置传值
            2. 通过生成器表达式
                列表推导式  [结果 for循环 if判断]
                集合推导式  {结果 for循环 if判断}
                字典推导式  {key:value for循环 if判断}

                生成器表达式: (结果 for循环 if判断)

            特点:
                1. 节省内存
                2. 惰性机制
                3. 只能向前不能反复

        lambda表达式
            lambda 参数: 返回值

        sorted, map, filter 把可迭代对象中的每一项数据传递给相对应的函数, 根据函数的返回值再进一步操作

        递归:
            函数自己调用自己.
            在python中递归是有最大深度限制的.

"""

type("")
