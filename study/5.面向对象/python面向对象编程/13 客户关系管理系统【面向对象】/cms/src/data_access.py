import os
import json
from conf.settings import CUSTOMERS_JSON_PATH
from loguru import logger


def loads_customers_json():
    customers = {}
    if os.path.exists(CUSTOMERS_JSON_PATH):
        with open(CUSTOMERS_JSON_PATH) as f:
            # json.loads(f.read())
            customers = json.load(f)

        logger.info(f"{CUSTOMERS_JSON_PATH}加载成功！")
    return customers


def save_customers(customers):
    # 数据持久化保存：json+文件操作
    with open(CUSTOMERS_JSON_PATH, "w") as f:
        # 对customers做序列化
        # f.write(json.dumps(customers))
        json.dump(customers, f)
