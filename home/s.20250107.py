# coding=UTF-8

from typing import Dict, List
import os

"""
写函数，检查传入字典的每一个value的长度,
如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
PS: 字典中的value只能是字符串或列表
"""


def check_value(data: Dict[str, ...]) -> Dict[str, ...]:
    for key, value in data.items():
        if len(value) > 2:
            data[key] = value[:2]
    return data

"""
写函数，此函数只接收一个参数且此参数必须是列表数据类型，
此函数完成的功能是返回给调用者一个字典，
此字典的键值对为此列表的索引及对应的元素。
例如
传入的列表为：[11, 22, 33]
返回的字典为
{0: 11, 1: 22, 2: 33}
"""


def convent_dict(data: List[...]) -> Dict[int, ...]:
    result = {}
    for index, value in enumerate(data):
        result[index] = value
    return result


"""
写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作。
"""


def write_file(filename: str, data: str) -> str:
    with open(filename, "w") as f:
        f.write(data)
    pwd = os.getcwd()
    return os.path.join(pwd, filename)



if __name__ == '__main__':
    data = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
    print(check_value(data))
    data2 = [11, 22, 33]
    print(convent_dict(data2))
    filename, data = "data.txt", "Hello World!"
    print(write_file(filename, data))