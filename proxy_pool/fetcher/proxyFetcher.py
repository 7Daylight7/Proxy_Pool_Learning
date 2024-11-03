"""
抓取免费代理网站代理
"""
import random
import time

from util.webRequest import WebRequest
from db.redisClient import RedisClient


def freeproxy01 (page_count=7):
    """
    云代理  "http://www.ip3366.net/"
    """
    start_url = "http://www.ip3366.net/free/"
    for page in range(1,page_count+1):
        page_url = start_url+f"?stype=1&page={page}"
        html_data = WebRequest().get(page_url).tree
        time.sleep(random.uniform(2,3))
        # print(html_data)
        trs = html_data.xpath("/html/body/div[2]/div/div[2]/table/tbody/tr")
        for tr in trs:
            ip = tr.xpath("./td[1]/text()")[0]
            port = tr.xpath("./td[2]/text()")[0]
            proxy = ip+":"+port
            # print(proxy)
            yield proxy

# 待处理 疑似js动态加载
def freeproxy02 (page_count = 10):
    """
    快代理  "https://www.kuaidaili.com/"
    """
    start_url = "https://www.kuaidaili.com/free/"

    for page in range(1,page_count+1):
        page_url = start_url+f"dps/{page}/"
        html_data = WebRequest().get(page_url).tree
        time.sleep(random.uniform(2,3))

        trs = html_data.xpath("/html/body/div[3]/main/div/section/div/div[2]/div/div/div[2]/div/table/tbody/tr")
        for tr in trs:
            ip = tr.xpath("./td[1]/text()")[0]
            port = tr.xpath("./td[2]/text()")[0]
            proxy = ip+":"+port
            print(proxy)
            yield proxy

def freeproxy03(page_count = 100):
    """
    89免费代理  "https://www.89ip.cn/"
    """
    start_url = "https://www.89ip.cn/"
    for page in range(1, page_count + 1):
        page_url = start_url + f"index_{page}.html"
        html_data = WebRequest().get(page_url).tree
        time.sleep(random.uniform(2, 3))

        trs = html_data.xpath('/html/body/meta"utf-8"/div[3]/div[1]/div/div[1]/table/tbody/tr')
        for tr in trs:
            ip = tr.xpath("./td[1]/text()")[0]
            port = tr.xpath("./td[2]/text()")[0]
            proxy = ip+":"+port
            yield proxy

proxy_func_list = [freeproxy01]

if __name__ == '__main__':
    client = RedisClient()
    for func in proxy_func_list:
        proxies = func()
        for one_proxy in proxies:
            # print("---代理写入数据库---")
            client.add(one_proxy)