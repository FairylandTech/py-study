a = int(input('请输入一个数字:'))
b = int(input('请输入一个数字:'))

result = a - b if a > b else b - a
result = (a - b) if a > b else (b - a)
print(result)
