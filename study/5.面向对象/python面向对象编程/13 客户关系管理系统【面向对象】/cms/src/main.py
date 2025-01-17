from src.data_access import loads_customers_json
from src.customer import CustomerManager
import sys
from loguru import logger

logger.add("logs/customers.log", level="DEBUG", rotation="200 MB")


def main():
    logger.info("程序启动")
    cm = CustomerManager()
    while 1:
        print("""
               1. 添加客户
               2. 删除客户
               3. 修改客户
               4. 查询一个客户
               5. 查询所有客户
               6. 保存
               7. 退出

            """)
        choice = input("请输入您的选择:")

        handler = {
            "1": cm.add_customer,
            "2": cm.del_customer,
            "3": cm.update_customer,
            "4": cm.query_one_customer,
            "5": cm.show_all_customers,
        }

        func = handler.get(choice)

        if func:
            func()
        else:
            logger.info("程序退出！")
            sys.exit(0)
