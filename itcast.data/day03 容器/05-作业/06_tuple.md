## 题目1 [加强训练]

### 题干

有如下两行代码：
tuple1 = (2)
tuple2 = (2,)
请问tuple1与tuple2有什么不同

### 训练目标

定义一个元素的元组

### 训练提示

通过肉眼能看到的只是一个逗号的区别，那么在python里面他是怎么理解的呢？

### 参考方案

用type（）方法来分别对这两个变量进行区别

### 操作步骤

用type(tuple1),与type(tuple12)的结果进行比较

### 参考答案

``` python
tuple1 = (2)
tuple2 = (2,)
print(type(tuple1))
print(type(tuple2))
# 对于tuple1 = （2），python解释器会将小括号理解成一个运算符号，那么这时候 返回的值是一个int类型
# 所以对于只有一个元素的元组来说，要创建一个元组，那么就必须要加逗号
```




## 题目2 [加强训练]

### 题干

有如下代码，请回答问题？

```python
my_tuple = ("itcast", "python", "CPP", 18, 3.14, True)
```

1.  使用下标的方法，输出元组中的元素 `"CPP"`
2.  使用 for 循环遍历元组
3.  使用 while 循环遍历元组

### 训练目标

1.  元组的下标操作
2.  元组的 for 循环遍历
3.  元组的 while 循环遍历

### 训练提示

1.  python 中的下标是从 0 开始，还是从 1 开始？
2.  如何进行 for 遍历？
3.  如何进行 while 遍历？while 的条件怎么写？


### 参考方案

1. 下标从 0 开始，故 CPP 的下标是 2
2. 使用 `for ... in ...` 遍历
3. while 循环，需要使用下标，判断条件可以借助 `len()`实现

### 操作步骤

1. 使用下标的方法，取 CPP 的值
2. for 循环遍历
3. while 循环遍历

### 参考答案

``` python
my_tuple = ("itcast", "python", "CPP", 18, 3.14, True)

# 1. 使用下标的方法，输出元组中的元素 `"CPP"`使用下标的方法，
result = my_tuple[2]
print(result)

# 2. 使用 for 循环遍历元组
for i in my_tuple:
    print(i)

print("-" * 20)

# 3. 使用 while 循环遍历元组
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1

```



