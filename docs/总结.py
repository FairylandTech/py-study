# #变量
# #一个可以变化的量，没有固定的值
# a = 1
# print(a)
# a = 2
# print(a)
# #上面每次重新赋值，a这个变量的值都会变化，这就是变量，值随时都可以变化，
# # python里也有常量，一般用大写字母标识用以区分，但是仍然可以通过重新赋值改变常量值，只是通过这种方式用来区分
# CHANG = 404
# print(CHANG)
# CHANG = 500
# print(CHANG)
# #python里一切皆对象，一个变量就可以理解为一个对象



# #数据类型
# # 字符串(关键字str)
# #被''或""或者三个''/""的数据是个字符串，里面可以是任何数据，
zifuchuan = '阿三，haha'
# print(zifuchuan)
# zifuchuan = "阿门，nihao"
# print(zifuchuan)
# zifuchuan = '''aaa'''
# print(zifuchuan)

#字符串是不可变数据类型，不能直接修改，但是可以通过重新赋值和一些方法改变，但那样是变成了一个新的字符串。
#字符串的一个特性，切片，  字符串[开头:结尾:步长]
#正序
#不输入开头结尾，默认全取，不输入步长，默认为1（即挨个取）
# zifuchuan = "阿门，nihao"
# qiepian = zifuchuan[::]
# print(qiepian)
#字符串里的开头和结尾是通过下标来取的，下标从0开始计，即第一个元素的下标是0，
# 步长是隔几个元素取的意思1就是挨个取，2就是隔2个，后续同理，超出范围的都不会取
#注意切片的开头和结尾是个左闭右开区间（包头不包尾）
# qiepian = zifuchuan[0:4:1]   #取到了 阿门，ni  但是输出没有i
# print(qiepian)
# qiepian = zifuchuan[0:4:2]
# print(qiepian)

#步长为负数，正数是从左往右取的，负数则是从右往左了        -----------------------------------------------------------------
# qiepian = zifuchuan[0:4:-1]
# print(qiepian)
# print(zifuchuan[0:4:-1])

#倒序，即开头和结尾为负数，下标变成了从右向左数，从-1开始计算，注意开头一定要小于结尾
# qiepian = zifuchuan[-1:-4:-1]
# print(qiepian)

#将字符串的逆序输出
# nixu =

# #字符串的方法
# #分割，split方法  --以XX为分割，会被分割为一个列表，默认有多少分割多少，可以限定分割次数
# zifuchuan = "阿门,nihao,ccd.加拿大"
# fenge = zifuchuan.split(",")
# print(fenge)
# fenge = zifuchuan.split(",",1)
# print(fenge)

# #拼接   用"+"
# str1 = 'hello'
# str2 = 'world'
# print(str1)
# print(str2)
# print(str1 + str2)

##替换，  replace
# zifuchuan = "阿门,nihao,ccd.加拿大"
# fenge = zifuchuan.replace(",","!")
# print(fenge)

# #添加， join(一次只能添加一个元素，多了会报错)
# zifuchuan = "阿门,nihao,ccd,加拿大"
# fenge = zifuchuan.join("死而复生")
# print(fenge)


# # 整型（关键字int）
# #就是一个整数，被字符串的符号包裹就是一个字符串类型，就不是整型了
# zheng = 5
# print(zheng)
# print(type(zheng))
# zhengshu = '5'
# print(zhengshu)
# print(type(zhengshu))

# #但是只有数字的字符串可以被转换为整数，有数字之外的会报错，有小数的会去掉小数点，只保留整数。
# zhengshu = '5'
# zhengshu = int(zhengshu)
# print(zhengshu)
# print(type(zhengshu))
# #整型可以被转换为浮点型，会在后面默认转换为一位小数
# print(float(zhengshu))

# # 浮点型
# #就是一个小数，被字符串的符号包裹就是一个字符串类型，就不是浮点型了
# fu = 5.12
# print(fu)
# print(type(fu))
# fudian = '5.12'
# print(fudian)
# print(type(fudian))

# #同理只有数字的字符串可以被转换为浮点型，没有小数点的同整数，有小数点的保留小数点。
# fu = '3.14159'
# fu = float(fu)
# print(fu)
# print(type(fu))
#
# fu = '3'
# fu = float(fu)
# print(fu)
# print(type(fu))


# # 列表(list)
# #列表的一个典型特征是[]，里面可以有多个值，里面的每个值可以是任何数据类型，
# # 值也叫元素，每个元素用","分隔开，最后一个元素不用加","
# liebiao = ['阿三，haha',123,5.12]
# #列表可以嵌套，就是在列表里放一个列表，列表里的一个列表是一个元素
# liebiao = ['阿三，haha',123,5.12,[33,"aecf",2.0],['按揭车',504,"wef"]]
# for i in liebiao:
#     print(i)

#列表的一些方法
#增
#append 将单个元素加在列表的最后面
# liebiao = ['阿三，haha',123,5.12]
# liebiao.append([33,"aecf",2.0])
# print(liebiao)
#insert  在指定下标

#extend


# # 元组
# # 字典
# # 集合