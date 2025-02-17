# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-12 22:07:39 UTC+08:00
"""

from codes.demo1.persion import Person
from codes.demo1.stu import Student
from codes.demo1.Tech import Teacher
from codes.demo1.administrator import Admin


def gerate_info(person: Person):
    person.show()


if __name__ == "__main__":
    student = Student("Tom", "2000-01-01", "男", "大一")
    teacher = Teacher("Lucy", "1980-01-01", "女", "高级")
    teacher1 = Teacher("三上老师", "1980-01-01", "女", "特级")
    admin = Admin("张妈", "1990-01-01", "男", "特级")

    gerate_info(student)
    gerate_info(teacher)
    gerate_info(teacher1)
    gerate_info(admin)
