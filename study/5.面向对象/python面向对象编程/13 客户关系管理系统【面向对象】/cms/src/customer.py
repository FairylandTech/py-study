from loguru import logger

from src.data_access import save_customers, loads_customers_json


class CustomerManager(object):
    customers = loads_customers_json()

    # 添加客户功能
    def add_customer(self):
        # (1) 添加客户 append

        id = input("请输入添加客户的ID:")

        if id in self.customers:  # "1001" in {1001:...}
            print("该ID已经存在！")
        else:

            name = input("请输入添加客户的姓名:")
            age = input("请输入添加客户的年龄:")
            email = input("请输入添加客户的邮箱:")

            new_customer = {
                "name": name,
                "age": age,
                "email": email
            }
            # customers[id] = new_customer
            self.customers.update({id: new_customer})

            # print(f"添加客户{name}成功！")
            logger.info(f"添加客户{name}成功！")
            print("当前客户:", self.customers)
            save_customers(self.customers)

    # 删除客户
    def del_customer(self):
        # (2) 删除客户
        del_customer_id = input("请输入删除客户的ID:")
        if del_customer_id in self.customers:

            self.customers.pop(del_customer_id)
            # print(f"删除{del_customer_id}客户成功!")
            logger.info(f"删除{del_customer_id}客户成功!")
            print("当前客户:", self.customers)

            save_customers(self.customers)
        else:
            print("该ID不存在！")

    # 修改客户
    def update_customer(self):
        # (3) 修改客户
        update_customer_id = input("请输入修改客户的ID:")

        if update_customer_id in self.customers:

            name = input("请输入修改客户新的姓名：")
            age = input("请输入修改客户新的年龄：")
            email = input("请输入修改客户新的邮箱：")

            self.customers[update_customer_id].update({"name": name, "age": age, "email": email})

            # print(f"{update_customer_id}客户修改成功！")
            logger.info(f"{update_customer_id}客户修改成功！")
            print("当前客户:", self.customers)

            save_customers(self.customers)

        else:
            print("该ID不存在！")

    # 查询一个客户

    def query_one_customer(self):
        # (4) 查看某一个客户
        query_customer_id = input("请输入查看客户的ID:")
        if query_customer_id in self.customers:
            customerD = self.customers[query_customer_id]
            print(f"姓名：{customerD.get('name')}，年龄：{customerD.get('age')}，邮箱：{customerD.get('email')}")
        else:
            print("该客户ID不存在！")

    def show_all_customers(self):
        # (5) 遍历每一个一个客户信息
        # if len(customers) == 0:
        if self.customers:
            for key, customerDict in self.customers.items():
                print(
                    f"客户ID：{key},姓名:{customerDict.get('name'):10},年龄：{customerDict.get('age')},邮箱:{customerDict.get('email')}")
        else:
            print("当前没有任何客户信息！")


