dict1 = {
    "name": "汪峰",
    "wife": {
        "name": "章子怡",
        "age": 18,
        'hobby': ['台球', "武术", "演戏"]
    },
    "hobby": ["唱歌", '跳舞', "当导师"],
    "children": [
        {"name": "老大", "age": 10},
        {"name": "老二", "age": 8},
    ]
}

# print(dict1)
# print(dict1['wife']['hobby'][1])

# # 给汪峰添加一个爱好, 卡拉ok
# dict1['hobby'].append("卡拉ok")
# print(dict1)

# 给汪峰的二儿子加一岁
dict1['children'][1]['age'] += 1
print(dict1)