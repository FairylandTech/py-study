# 1. 从服务器获取到网页源代码(urllib.request)
from urllib.request import Request, urlopen
import re

def get_page(url):
    # 1. 准备请求信息
    r = Request(url, headers={
        # 模拟浏览器
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    })
    resp = urlopen(r)  # 发送请求
    return resp.read().decode("utf-8")

# 2. 从网页源代码中提取到你想要的数据(re)
#   先准备好re
def parse_page(s):
    obj = re.compile(r'<div class="item">.*?<em class="">(?P<rate>.*?)</em>.*?<span'
                     r' class="title">(?P<movie>.*?)</span>.*?<span class="rating_num"'
                     r' property="v:average">(?P<rating_num>.*?)</span>.*?<spa'
                     r'n>(?P<person_num>.*?)人评价</span>', re.S)  # re.S可以让正则中的.匹配换行符

    res = obj.finditer(s)  # 匹配
    lst = []
    for item in res:  # 循环结果
        dic = item.groupdict()  # 每次循环都是一个电影信息
        lst.append(dic)
    return lst

def main():
    f = open("movie.txt", mode="w", encoding="utf-8")
    for i in range(10):
        s = get_page(f"https://movie.douban.com/top250?start={i * 25}&filter=")
        result = parse_page(s)
        for d in result:
            f.write(str(d))
            f.write("\n")


main()
