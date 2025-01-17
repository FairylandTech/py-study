# 想要使用模块中的内容,必须先导入模块
# 方法一  import 模块名
# 使用:  模块名.功能名
# import my_module1
#
# print(my_module1.num)  # 使用my_module1中的变量num
# my_module1.func()   # 调用my_module1中 func函数
# dog = my_module1.Dog()  # 调用my_module1中的类创建对象
# dog.show_info()

# 方法二  from 模块名 import 功能名1, 功能名2, ....
# 使用: 功能名
# 注意点: 如果存在同名的方法名,则会被覆盖
# from my_module2 import func, num
# from my_module1 import num
# func()
# print(num)

# 方法三  from 模块名 import *   # 将模块中所有的功能进行导入
# 使用: 功能名
# from my_module2 import *
#
# print(num)
# func()
# dog = Dog()
# dog.show_info()

# as 起别名.可以对模块和功能起别名,
# 注意: 如果使用as别名,就不能再使用原来的名字
import my_module1 as mm1
from my_module1 import func as m1_func
from my_module2 import func as m2_func
mm1.func()
m1_func()
m2_func()

