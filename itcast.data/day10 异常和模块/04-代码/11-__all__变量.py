"""
__all__ 变量,可以在每个代码文件中(模块中)定义, 类型是元组,列表
作用: 影响 form 模块名 import * 导入行为,另外两种导入行为不受影响
1. 如果没有定义__all__ 变量, 模块中的所有功能,都可以被导入
2. 如果定义__all__ 变量,只能导入 变量中定义的内容
"""
from my_module3 import *

print(num)
func()
dog = Dog()   # 会报错
dog.show_info()

