# coding=UTF-8

# 基于字典的客户信息管理系统
#            1. 添加客户
#            2. 删除客户
#            3. 修改客户
#            4. 查询一个客户
#            5. 查询所有客户
#            6. 退出
# name = input("请输入添加客户的姓名:")
# age = input("请输入添加客户的年龄:")
# email = input("请输入添加客户的邮箱:")

import json
import os
from typing import List, Dict

USERS = []
FILE_PATH = "User.json"
ENCODING = "UTF-8"

def load_users(file_path: str) -> List[Dict[str, str]]:
    """
    读取文件中的用户信息
    :param file_path: 文件路径
    :return: 读取文件后的python对象
    """
    if not os.path.isfile(file_path):
        return []

    with open(file_path, "r", encoding=ENCODING) as user_stream:
        data = json.load(user_stream)

    return data

def save_users(file_path: str, data: List[Dict[str, str]]):
    try:
        with open(file_path, "w", encoding=ENCODING) as user_stream:
            json.dump(data, user_stream, indent=4, ensure_ascii=False)

        return True
    except Exception as e:
        print(e)
        return False


def add_user(name: str, age:str, email:str):
    users: List[Dict[str, str]] = load_users(FILE_PATH)
    user = {
        "name": name,
        "age": age,
        "email": email
    }
    users.append(user)
    if save_users(FILE_PATH, users):
        return True
    else:
        raise RuntimeError("写入文件失败...")

def delete_user(name: str):
    users = load_users(FILE_PATH)
    users_mapping = {user.get("name"): user for user in users}
    user = users_mapping.get(name)
    if user:
        users.remove(user)
        if save_users(FILE_PATH, users):
            return True
        else:
            raise RuntimeError("写入文件失败...")
    else:
        print("该用户不存在!")
        return False



def query_user(name: str=None):
    users = load_users(FILE_PATH)
    if not name:
        for user in users:
            user_str= f"姓名: {user.get('name')}, 年龄: {user.get('age')}, 邮件: {user.get('email')}"
            print(user_str)
    else:
        users_mapping = {user.get("name"): user for user in users}
        user = users_mapping.get(name)
        if user:
            user_str= f"姓名: {user.get('name')}, 年龄: {user.get('age')}, 邮件: {user.get('email')}"
            print(user_str)
        else:
            print("该用户不存在!")

def update_user(old, new, age, email):
    users = load_users(FILE_PATH)
    users_mapping = {user.get("name"): user for user in users}
    old_user = users_mapping.get(old)
    new_user = {
        "name": new,
        "age": age,
        "email": email
    }
    users.remove(old_user)
    users.append(new_user)
    if save_users(FILE_PATH, users):
        return True
    else:
        raise RuntimeError("写入文件失败...")



def main():
    while True:
        print("基于字典的客户信息管理系统")
        print("1. 添加客户")
        print("2. 删除客户")
        print("3. 修改客户")
        print("4. 查询一个客户")
        print("5. 查询所有客户")
        print("6. 退出")
        choise = int(input("请输入操作选项: "))
        if choise == 1:
            print("添加用户".center(50, "-"))
            name = input("姓名: ")
            age = input("年龄: ")
            eamil = input("邮件: ")
            if add_user(name, age, eamil):
                print("添加成功")
                print("".center(50, "-"))
            else:
                print("添加失败")
        elif choise == 2:
            print("删除用户".center(50, "-"))
            name = input("姓名: ")
            if delete_user(name):
                print("删除成功")
                print("".center(50, "-"))
            else:
                print("删除失败")
        elif choise == 3:
            print("修改用户".center(50, "-"))
            old_name = input("旧名字: ")
            new_name = input("新名字: ")
            age = input("新年龄: ")
            eamil = input("新邮箱: ")
            if update_user(old_name, new_name, age, eamil):
                print("修改成功")
                print("".center(50, "-"))
            else:
                print("修改失败")
        elif choise == 4:
            print("查询用户".center(50, "-"))
            name = input("姓名: ")
            query_user(name)
            print("".center(50, "-"))
        elif choise == 5:
            print("查询所有用户".center(50, "-"))
            query_user()
            print("".center(50, "-"))
        elif choise == 6:
            break
        else:
            print("输入错误, 请重新输入!")

if __name__ == '__main__':
    main()