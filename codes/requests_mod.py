# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-17 21:50:28 UTC+08:00
"""

"""
URL 由什么组成: http/https/webserver/sockt/sock5/ws/ftp/sftp  # 传输协议
    baidu.com/www.baidu.com/cnblog.cn  # 主机地址:端口
    http:80
    https:443
    /api/example/test  # 路径
    
    MySQL: 3306
    Redis: 6379
    PostgreSQL: 5432
    FTP: 21
    SSH: 22
    Telent: 23
    RDP: 3389
    Django: 8000
    Flask: 5000
    FastAPI: 3000
    nodejs/vue: 8080

"""

import requests  # 请求API, 访问 https://baidu.com

response = requests.request(method="GET", url="http://127.0.0.1:8000/api/example/test")  # response 一个对象

json_data = response.json()

print(json_data.get("code"))


print(json_data)

# requests.get() == requests.request(method="GET")
# requests.post() == requests.request(method="POST")


requests.get(
    url=url,
    params={},
    verify=False,
)
