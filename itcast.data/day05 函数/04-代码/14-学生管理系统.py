# 定义学生列表,保存所有的学生信息
stu_list = []


def show_menu():
    print('1. 添加学生')
    print('2. 删除学生')
    print('3. 修改学生信息')
    print('4. 查询单个学生信息')
    print('5. 查询所有的学生信息')
    print('6. 退出系统')


def insert_student():
    # 1. 通过 input 函数获取学生的信息, 姓名, 年龄, 性别
    name = input('请输入学生名字:')
    # [{}, {}, {}]  判断的是字典中的 value 是否存在
    for stu in stu_list:
        if stu['name'] == name:
            print('----------学生信息存在---------')
            return  # 结束函数的执行

    age = input('请输入学生年龄:')
    gender = input('请输入学生性别:')
    # 2. 将学生信息转换为字典进行保存
    stu_dict = {'name': name, 'age': int(age), 'gender': gender}
    # 3. 将这个学生字典添加的列表中
    stu_list.append(stu_dict)
    print('==============学生信息添加成功====================')


def remove_student():
    # 1. 使用 input 获取要删除 /修改/查询 的学生姓名
    name = input('请输入要操作的学生的名字:')
    # 2. 判断学生信息是否存在
    for stu in stu_list:
        if stu['name'] == name:
            # 3. 学生存在,对学生进行 删除 /修改/查询 操作
            stu_list.remove(stu)
            # return
            break
    # 4. 学生信息不存在,直接结束
    else:
        print('***********该学生信息不存在,无法删除**************')


def modify_student():
    # 1. 使用 input 获取要删除 /修改/查询 的学生姓名
    name = input('请输入要操作的学生的名字:')
    # 2. 判断学生信息是否存在
    for stu in stu_list:
        if stu['name'] == name:
            # 3. 学生存在,对学生进行 删除 /修改/查询 操作
            stu['age'] = int(input('请输入新的年龄:'))
            # return
            break
    # 4. 学生信息不存在,直接结束
    else:
        print('***********该学生信息不存在,无法修改**************')


def search_student():
    # 1. 使用 input 获取要删除 /修改/查询 的学生姓名
    name = input('请输入要操作的学生的名字:')
    # 2. 判断学生信息是否存在
    for stu in stu_list:
        if stu['name'] == name:
            # 3. 学生存在,对学生进行 删除 /修改/查询 操作
            print(f'姓名:{stu["name"]}, 年龄:{stu["age"]}, 性别:{stu["gender"]}')
            # return
            break
    # 4. 学生信息不存在,直接结束
    else:
        print('***********该学生信息不存在**************')


def show_all_info():
    if len(stu_list) > 0:
        for stu in stu_list:
            print(f'姓名:{stu["name"]}, 年龄:{stu["age"]}, 性别:{stu["gender"]}')
            # print(stu)
    else:
        print('目前没有学生信息')


def main():
    while True:
        show_menu()
        opt = input('请输入用来选择的操作编号:')
        if opt == '1':
            # print('1. 添加学生')
            insert_student()
        elif opt == '2':
            # print('2. 删除学生')
            remove_student()
        elif opt == '3':
            # print('3. 修改学生信息')
            modify_student()
        elif opt == '4':
            # print('4. 查询单个学生信息')
            search_student()
        elif opt == '5':
            # print('5. 查询所有的学生信息')
            show_all_info()
        elif opt == '6':
            print('欢迎下次使用本系统......')
            break
        else:
            print('输入有误,请再次输入')
            continue

        input('...... 回车键继续操作.......')


main()
