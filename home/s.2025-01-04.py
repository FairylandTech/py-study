# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-01-06 10:45:06 UTC+08:00
"""

# 基于字典的客户信息管理系统
# 1. 添加客户
# 2. 删除客户
# 3. 修改客户
# 4. 查询一个客户
# 5. 查询所有客户
# 6. 退出

import json
from dataclasses import dataclass, asdict
from typing import Sequence, List, Dict, MutableSequence, Self, Union


@dataclass(frozen=False)
class User:
    name: str
    age: str
    email: str
    sex: str

    def __str__(self: Self):
        return f"姓名: {self.name}, 年龄: {self.age}, 邮箱: {self.email}, 性别: {self.sex}"

    @property
    def to_dict(self: Self) -> Dict[str, ...]:
        return asdict(self)


class UserInfoManager:

    def __init__(self: Self, path: str):
        self.path: str = path
        self.users: MutableSequence[User] = []
        self.encoding: str = "UTF-8"

    def read(self: Self) -> MutableSequence[User]:
        with open(self.path, "r", encoding=self.encoding) as stream:
            data: List[Dict[str, ...]] = json.load(stream)
        if not data:
            return []
        else:
            return [User(user.get("name"), user.get("age"), user.get("email"), user.get("sex")) for user in data]

    def write(self: Self, users: Sequence[User]):
        with open(self.path, "w", encoding=self.encoding) as stream:
            json.dump([user.to_dict for user in users], stream, ensure_ascii=False, indent=2)

    def query(self, name: str = None) -> Union[Sequence[User], None]:
        self.users: Sequence[User] = self.read()
        if not name:
            return tuple(self.users)
        else:
            user_mapping: Dict[str, User] = {user.name: user for user in self.users}
            return (user_mapping.get(name),) if user_mapping.get(name, None) else None

    def add(self: Self, user: User):
        self.users = self.read()
        for userc in self.users:
            if userc.name == user.name:
                return False
        self.users.append(user)
        self.write(self.users)
        return True

    def delete(self: Self, name: str):
        self.users = self.read()
        for user in self.users:
            if user.name == name:
                self.users.remove(user)
                self.write(self.users)
                return True
        return False

    def update(self: Self, name, user: User):
        self.users = self.read()
        for userc in self.users:
            if userc.name == name:
                userc.name = user.name
                userc.age = user.age
                userc.email = user.email
                userc.sex = user.sex
                self.write(self.users)
                return True
        return False


def main():
    while True:
        database = "customer.json"
        print("客户信息管理系统")
        print("1. 添加客户")
        print("2. 删除客户")
        print("3. 修改客户")
        print("4. 查询一个客户")
        print("5. 查询所有客户")
        print("6. 退出")
        choice = int(input("请选择操作: "))
        if choice == 1:
            print("添加客户")
            name = input("请输入添加客户的姓名: ")
            age = input("请输入添加客户的年龄: ")
            email = input("请输入添加客户的邮箱: ")
            sex = input("请输入添加客户的性别: ")
            user = User(name, age, email, sex)
            user_info_manager = UserInfoManager(database)
            flag = user_info_manager.add(user)
            if flag:
                print("添加成功")
            else:
                print("添加失败")
            print()
        elif choice == 2:
            name = input("请输入删除的客户姓名: ")
            user_info_manager = UserInfoManager(database)
            flag = user_info_manager.delete(name)
            if flag:
                print("删除成功")
            else:
                print("删除失败")
            print()
            pass
        elif choice == 3:
            old_name = input("请输入修改的客户姓名: ")
            name = input("请输入修改的客户姓名(新): ")
            age = input("请输入修改的客户年龄(新): ")
            email = input("请输入修改的客户邮箱(新): ")
            sex = input("请输入添加客户的性别(新): ")
            user = User(name, age, email, sex)
            user_info_manager = UserInfoManager(database)
            flag = user_info_manager.update(old_name, user)
            if flag:
                print("修改成功")
            else:
                print("修改失败")
            print()
            pass
        elif choice == 4:
            name = input("请输入查询的客户姓名: ")
            user_info_manager = UserInfoManager(database)
            (user,) = user_info_manager.query(name)
            if user:
                print(str(user))
            else:
                print("没有找到该客户")
            print()
            pass
        elif choice == 5:
            print("查询所有客户")
            user_info_manager = UserInfoManager(database)
            users = user_info_manager.query()
            for user in users:
                print(str(user))
            print("查询成功")
            print()
        elif choice == 6:
            print()
            break
        else:
            print("输入错误, 请重新输入")


if __name__ == "__main__":
    main()
