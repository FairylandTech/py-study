# 方法一  import 包名.模块名
# import my_package.my_module1
# import my_package.my_module2 as mm2
#
# my_package.my_module1.func()
# mm2.func()

# 方法2  from 包名.模块名 import 功能名
# from my_package.my_module1 import func
# from my_package.my_module2 import *
# func()

# 方法三 from 包名 import *  # 导入的是__init__.py中的内容
from my_package import *
func()
