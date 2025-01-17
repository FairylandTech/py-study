import os


def create_files():
    for i in range(10):
        file_name = 'test/file_' + str(i) + '.txt'
        print(file_name)
        f = open(file_name, 'w')
        f.close()


def create_files_1():
    os.chdir('test')
    for i in range(10, 20):
        file_name = 'file_' + str(i) + '.txt'
        print(file_name)
        f = open(file_name, 'w')
        f.close()
    os.chdir('../')  # ../ 上一级目录


def modify_filename():
    os.chdir('test')
    buf_list = os.listdir()
    # print(buf_list)
    for file in buf_list:
        new_file = 'py43_' + file
        os.rename(file, new_file)

    os.chdir('../')


def modify_filename_1():
    os.chdir('test')
    buf_list = os.listdir()
    # print(buf_list)
    for file in buf_list:
        num = len('py43_')
        new_file = file[num:]
        os.rename(file, new_file)

    os.chdir('../')


# create_files()
# create_files_1()
# modify_filename()
modify_filename_1()
