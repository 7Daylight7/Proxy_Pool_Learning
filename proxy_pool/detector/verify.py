"""
    检测模块
    从数据库中获取所有代理，挨个检测
"""
import requests
from db.redisClient import RedisClient
import concurrent.futures
from settings import VERIFY_URL,VERIFY_TIMEOUT
from util.webRequest import WebRequest

# 实例化redis数据库模块对象
client = RedisClient()

def verify_proxy(proxy):
    """
    检测代理是否可用
    """
    proxies = {
        "http":"http://"+ proxy,
        "https":"https://"+ proxy
    }
    headers = WebRequest().header

    try:
        resp = requests.get(url = VERIFY_URL, headers= headers, proxies=proxies, timeout=VERIFY_TIMEOUT)
        if resp.status_code in [200,206,302]:  # 判断请求是否可行
            client.max(proxy)
            print("-----代理可用-----",proxy)
        else:
            client.decrease(proxy)  # 请求不成功,表示代码不可用
            print("-----请求状态码不合法-----",proxy)
    except:
        client.decrease(proxy)  # 请求超时表示代理不可靠
        print("-----请求超时-----",proxy)

def verify_thread_pool():
    """线程池测试代理"""
    # 1.从数据库中取到所有代理
    proxies_list = client.all()
    # 2.用线程池检测代理
    with concurrent.futures.ThreadPoolExecutor(max_workers=10)as executor:
        for proxy in proxies_list:
            executor.submit(verify_proxy,proxy)


if __name__ == '__main__':
    verify_thread_pool()


