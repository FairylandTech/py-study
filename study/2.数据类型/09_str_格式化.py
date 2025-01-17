name = "sylar"
age = 18
s = "我叫%s, 我今年%d岁了" % (name, age)  # 必须会
print(s)

s2 = f"我叫{name}, 我今年{age}岁了"  # 主推
print(s2)

s3 = "我叫{}, 我今年{}岁了".format(name, age)
print(s3)

s4 = "我叫{1}, 我今年{0}岁了".format(age, name)
print(s4)

s5 = "我叫{aname}, 我今年{aage}岁了".format(aname=name, aage=age)
print(s5)
