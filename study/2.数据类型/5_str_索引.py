s = "我喜欢你"

# s1 = s[4]  # string index out of range
# print(s1)

print(s[-5])

import requests
resp = requests.get("url")
print(resp.text)  # 返回的响应信息
