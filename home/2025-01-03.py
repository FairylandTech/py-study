'''等级 1：
1  变量赋值：创建一个变量name，并将你的名字作为字符串赋值给它，然后打印"Hello, name!"。'''
name = '马麟'
print(f'Hello,{name}')
'''2  简单计算：计算并打印7 + 5的结果。'''
print(7+5)
'''3  列表创建：创建一个列表colors，包含"红色"、"绿色"和"蓝色"。'''
colors = ["红色","绿色","蓝色"]
'''4  类型转换：将字符串类型的数字"123"转换为整数类型，并打印结果。'''
string = '123'
int_str = int(string)
print(int_str)
'''5  if语句：编写一个if语句，判断变量age是否大于等于18，如果是，打印"成年""成年"'''
age = 22
if age > 18:
    print("成年")

'''6  for循环：使用for循环打印数字1到5。'''
for number in range(0,5):
    print(number)
'''7  字符串操作：创建一个字符串text，内容为"Python is fun"，将其全部转换为大写，并打印结果。'''
text = "Python is fun"
print(repr(text.upper()))
'''8  简单函数：定义一个函数greet()，该函数打印"Welcome to Python!"。'''
def greet()
    print("Welcome to Python!")
greet()
'''9  输入输出：使用input()函数获取用户的年龄，并打印"你今年X岁"，其中X是用户输入的年龄。'''
age = input('你的年龄是：')
print(f"你今年{age}岁")
'''10  逻辑判断：检查变量number是否为偶数，如果是，打印"偶数"，否则打印"奇数"。'''
number = 30
if number%2 == 0:
    print("偶数")
else:
    print("奇数")




'''等级 2：
1  字典使用：创建一个字典student，包含键值对："姓名"对应你的名字，"学号"对应任意数字。'''
student = {"姓名":"马麟","学号":123}
'''2  列表操作：给定列表numbers = [2, 4, 6, 8]，计算所有元素的和。'''
numbers = [2, 4, 6, 8]
num = 0
for number in numbers:
    num += number
print(num)
'''3  for循环嵌套：使用两个for循环，打印一个3x3的星号矩阵。'''
for i in range(0,3):
    print('*')
    for j in (0,3):
        print('*')

'''4  if...else语句：编写程序，判断用户输入的数字是正数、负数还是零，并打印相应信息。'''
number = int(input('请输入一个整数：'))
if number > 0:
    print('正数')
elif number < 0:
    print('负数')
else:
    print('零')
'''5  函数参数：定义一个函数add(a, b)，返回两个参数的和。'''
def add(a,b):
    return a+b
add(3,5)
'''6  列表推导式：使用列表推导式生成一个包含1到10之间所有偶数的列表。'''
num_list = [].append(i for i in range(0,10) if i%2 == 0)
'''7  字符串格式化：使用format()方法，将变量name和age格式化到字符串"我是{name}，今年{age}岁"中。'''
name = '马麟'
age = 22
print("我是{}，今年{}岁".format(name,age))
'''8  while循环：使用while循环，计算1到100的累计和。'''
count = 0
number = 1
while number < 101:
    count += number
    num += 1
'''9  类型判断：编写程序，判断输入的数据是字符串、整数还是浮点数。'''
data = input('请输入数据：')
try:
    if int(data) is True:
        print('你输入的数据是整数')
except Exception as e:
    try:
        if float(data) is True:
            print('你输入的数据是浮点数')
    except Exception as e:
        print('你输入的数据是字符串')

'''10  模块导入：导入math模块，使用sqrt()函数计算16的平方根。'''





'''等级 3：
1  列表排序：给定列表scores = [88, 92, 75, 83, 95]，按从高到低排序并打印结果。'''
scores = [88, 92, 75, 83, 95]
scores.sort(reverse=True)
print(scores)
'''2  文件读写：创建一个文本文件，写入一句话，然后读取并打印文件内容。'''

'''3  异常处理：编写程序，除以用户输入的数字，如果输入为零，捕获异常并打印"不能除以零"。'''
number = int(input('请输入除数：'))
chu_number = 100
try:
    shang = chu_number/number
except Exception as e:
    print("不能除以零")
'''4  函数返回多个值：定义函数calculate(a, b)，返回a和b的和、差、积、商。'''
def calculate(a, b):
    num = a + b
    cha = a - b
    ji = a*b
    shang = a/b
    fan_hui = f'和为{num}差为{cha}积为{ji}商为{shang}'
    return
'''5  匿名函数：使用lambda函数，实现两个数相加，并打印结果。'''

'''6  集合操作：创建两个集合，求它们的并集和交集。'''
set1 = {2,6,9,7,5}
set2 = {3,9,4,6,5}
jiao = set1 | set2
bing = set1 & set2
print(jiao)
print(bing)
'''7  字典推导式：给定列表keys = ['a', 'b', 'c']和values = [1, 2, 3]，生成对应的字典。'''
keys = ['a', 'b', 'c']
values = [1, 2, 3]
# dict1 = {}.update(key value for key value in )
'''8  多重条件判断：编写程序，根据用户的考试成绩打印等级：90分以上"优秀"，80-89分"良好"，
70-79分"中等"，60-69分"及格"，60分以下"不及格"。'''
scores = 88
if scores >= 90:
    print("优秀")
elif 80 <= scores <=89:
    print("良好")
elif 70 <= scores <=79:
    print("中等")
elif 60 <= scores <=69:
    print("及格")
else:
    print("不及格")

'''9  列表去重：给定列表nums = [1, 2, 2, 3, 4, 4, 5]，去除重复元素并打印新列表。'''
nums = [1, 2, 2, 3, 4, 4, 5]
set_list = list(set(nums))
set_list.sort(reverse=False)
print(set_list)
'''10  递归函数：编写递归函数计算n的阶乘。'''
def jie_cheng(number):
    numbers = number
    num = 1
    while numbers >0:
        num = num*numbers
        numbers -= 1
    return num

print(jie_cheng(3))



'''等级 4：
1  字符串统计：输入一段字符串，统计其中英文字母、数字、空格和其他字符的个数。'''
import string
count_str = input('请输入：')
zimu = 0
number = 0
kong_ge = 0
qi_ta = 0
for i in count_str:
    if i in string.ascii_letters:
        zimu += 1
    elif i in string.digits:
        number += 1
    elif i == ' ':
        kong_ge += 1
    else:
        qi_ta += 1
print(f'英文字母有{zimu}个数，数字有{number}个，空格有{kong_ge}个，其他字符有{qi_ta}个')

'''2  冒泡排序：实现冒泡排序算法，对列表[5, 2, 9, 1, 5, 6]进行排序。'''
num_list = [5, 2, 9, 1, 5, 6]
mao_list = []
for number in num_list:
    suo_yin = 
    for hou_number in num_list:

'''3  读取CSV文件：使用csv模块读取一个CSV文件，并打印每一行内容（假设文件存在）。'''

'''4  日期和时间：导入datetime模块，获取当前日期和时间，格式化输出为"YYYY-MM-DD HH:MM:SS"。'''

'''5  面向对象编程：定义一个Person类，包含属性name和age，以及方法say_hello()，实例化对象并调用方法。'''

'''6  函数参数解包：编写函数，接受不定数量的关键字参数，并打印所有键值对。'''

'''7  正则表达式：使用re模块，验证用户输入的手机号是否符合格式（假设格式为11位数字，以1开头）。'''

'''8  JSON数据处理：将字典{"name": "Alice", "age": 25}转换为JSON字符串，并打印结果。'''

'''9  生成器：编写一个生成器函数，依次返回指定范围内的质数。'''

'''10  上下文管理器：使用with语句打开文件，读取内容并打印。'''