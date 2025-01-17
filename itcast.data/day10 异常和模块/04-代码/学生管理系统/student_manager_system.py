import student


class StudentManagerSystem(object):
    def __init__(self):
        self.stu_dicts = {}

    @staticmethod
    def __show_menu():
        print('1. 添加学生')
        print('2. 删除学生')
        print('3. 修改学生信息')
        print('4. 查询单个学生信息')
        print('5. 查询所有的学生信息')
        print('6. 退出系统')

    def __insert_student(self):
        # 1. 使用 input 获取学生的信息
        stu_id = input('请输入学生学号:')
        # 代码优化, 判断学生信息是否存在, 学号是否存在. 判断字典的key是否存在
        if stu_id in self.stu_dicts:  # key存在返回True
            print('学生信息已经存在, 不需要再次添加.........')
            return
        name = input('请输入学生名字:')
        age = input('请输入学生年龄:')
        gender = input('请输入学生性别:')

        # 2. 使用学生信息,创建学生对象  学生类(参数)
        stu = student.Student(stu_id, name, age, gender)
        # 3. 将学生对象添加的字典中 字典['key'] = 数据值
        self.stu_dicts[stu_id] = stu

    def __remove_student(self):
        # 1. 使用 input 输入学生学号
        stu_id = input('请输入学号:')
        # 2. 判断学生信息是否存在
        if stu_id in self.stu_dicts:
            # 3. 存在进行操作, 删除字典中的数据,  del 变量[key]
            del self.stu_dicts[stu_id]
            print('学生已经删除')
        else:
            print('学生信息不存在,无法删除.....')

    def __modify_student(self):
        # 1. 使用 input 输入学生学号
        stu_id = input('请输入学号:')
        # 2. 判断学生信息是否存在
        if stu_id in self.stu_dicts:
            # 修改对象的属性  对象.属性名 = 属性值
            stu = self.stu_dicts[stu_id]  # 字典[key]
            stu.age = input('请输入新的年龄:')
            print('信息已经修改完毕.....')
        else:
            print('学生信息不存在,无法删除.....')

    def __search_student(self):
        # 1. 使用 input 输入学生学号
        stu_id = input('请输入学号:')
        # 2. 判断学生信息是否存在
        if stu_id in self.stu_dicts:
            # 修改对象的属性  对象.属性名 = 属性值
            stu = self.stu_dicts[stu_id]  # 字典[key]
            print(stu)
        else:
            print('学生信息不存在,无法删除.....')

    def __show_all_info(self):
        for stu in self.stu_dicts.values():
            print(stu)

    def __save(self):
        f = open('student.txt', 'w', encoding='utf-8')
        for stu in self.stu_dicts.values():
            f.write(str(stu) + '\n')  # str(stu) 调用 student类中的__str__ 方法
        f.close()

    def __load_info(self):
        try:
            f = open('student.txt', 'r', encoding='utf-8')
            buf_list = f.readlines()
            for buf in buf_list:
                buf = buf.strip()  # 去重\n
                info_list = buf.split(',')  # 列表
                # 创建对象
                # stu = student.Student(info_list[0], info_list[1], info_list[2], info_list[3])
                stu = student.Student(*info_list)
                #  将对象添加到字典中
                stu_id = info_list[0]
                self.stu_dicts[stu_id] = stu
            f.close()
        except Exception:
            pass

    def start(self):
        self.__load_info()
        while True:
            self.__show_menu()
            opt = input('请输入用来选择的操作编号:')
            if opt == '1':
                # print('1. 添加学生')
                self.__insert_student()
            elif opt == '2':
                # print('2. 删除学生')
                self.__remove_student()
            elif opt == '3':
                # print('3. 修改学生信息')
                self.__modify_student()
            elif opt == '4':
                # print('4. 查询单个学生信息')
                self.__search_student()
            elif opt == '5':
                # print('5. 查询所有的学生信息')
                self.__show_all_info()
            elif opt == '6':
                self.__save()
                print('欢迎下次使用本系统......')
                break
            else:
                print('输入有误,请再次输入')
                continue

            input('...... 回车键继续操作.......')
