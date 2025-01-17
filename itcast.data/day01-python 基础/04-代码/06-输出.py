# 在python中的输出使用print函数
# 基本输出
print('hello')   # 会输出 hello
print(123)   # 会输出 123

# 一次输出多个内容
print('isaac', 18)  # 会输出 isaac 和18 ,两者之间使用 空格隔开

# 可以书写表达式
print(1 + 2)  # 会输出 1 +2 的结果 3

# 格式化输出, 格式化占位符(坑位), %s 字符串 %d int 整数int  %f  小数浮点数float
name = 'isaac'
# 需求: 输出 我的名字是xxx,我很开心
print("我的名字是%s,我很开心." % name)

age = 18
# 需求: 输出 我的年龄是18岁
print('我的年龄是%d岁' % age)

height = 170.5
# %f 输出小数,默认保留6位小数
print('我的身高是%f cm' % height)  # Ctrl d 快速的复制一行代码, shift enter  在下方新建一行代码
# %.nf  保留n 位小数
print('我的身高是%.1f cm' % height)
print('我的身高是%.2f cm' % height)

# 需求: 我的名字是xx,年龄是xx岁, 身高是xxcm
print('我的名字是%s,年龄是%d岁, 身高是%fcm' % (name, age, height))

# 输出50%, 使用格式化输出的时候,想要输出一个%, 需要使用两个%
print('及格人数占比为%d%%' % 50)

# python3.6版本开始支持 f-string ,占位统一使用 {} 占位,填充的数据直接写在 {} 里边
print(f"我的名字是{name},年龄是{age}岁, 身高是{height}cm")


# 转义字符 \n  将\和n组合在一块,作为一个字符使用, \n 代表换行
# print()函数输出之后,默认会添加一个换行, 如果不想要这个换行可以去掉
# print('hello', end=' ')
print('hello', end='_*_')
print('hello', end='')
print('world')
print('good good study\nday day up')
