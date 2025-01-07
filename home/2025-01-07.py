'''写函数，检查传入字典的每一个value的长度,
如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
PS: 字典中的value只能是字符串或列表'''
dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
# for i in dic:
#     print(i)
def unify_length_dict(a_dict):
    for key in a_dict:
        if len(a_dict[key]) >= 2:
            try:
                if str(a_dict[key]):
                    a_dict[key] = a_dict[key][0:2]
            except Exception as e:
                if list(a_dict[key]):
                    a_dict[key] = a_dict[key][0:2]
    return a_dict


print(unify_length_dict(dic))


'''写函数，此函数只接收一个参数且此参数必须是列表数据类型，
此函数完成的功能是返回给调用者一个字典，
此字典的键值对为此列表的索引及对应的元素。
例如
传入的列表为：[11, 22, 33]
返回的字典为
{0: 11, 1: 22, 2: 33}'''

lis = [11, 22, 33]
def list_index_dict(a_list):
    index_dict = {}
    for element in a_list:
        index = a_list.index(element)
        index_dict[index] = element
    return index_dict


print(list_index_dict(lis))

'''写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作。'''

def change_file(file_name,content):
    with open(f'{file_name}','a',encoding='utf-8') as file:
        file.write(content)
change_file('test.txt','Hello World')