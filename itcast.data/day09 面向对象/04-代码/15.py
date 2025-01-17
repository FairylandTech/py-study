# for i in range(5):
#     print('跑圈......')
#     for j in range(5):
#         if j == 2:
#             break
#         print('俯卧撑...')

# my_list = [11,22,33,44,55,66,77,88,99,90]
# my_dict = {'key1': [], 'key2': []}
# for i in my_list:
#     if i > 66:
#         my_dict['key1'].append(i)
#     else:
#         my_dict['key2'].append(i)
#
# print(my_dict)


my_str = 'hello world'
my_dict = {}
for i in my_str:
    if i == ' ':
        continue
    my_dict[i] = my_str.count(i)

print(my_dict)