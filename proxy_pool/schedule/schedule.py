"""
调度模块
"""
import time
from db.redisClient import RedisClient
from detector.verify import verify_thread_pool
from fetcher.proxyFetcher import proxy_func_list
import multiprocessing
from settings import GETTER_PROXY,VERIFY_PROXY
from api.proxyApi import app

client = RedisClient()

class Schedule:

    # 1.调度获取代理模块
    def getter_proxy(self):
        while True:
            for func in proxy_func_list:
                proxies = func()
                for proxy in proxies:
                    client.add(proxy)
            time.sleep(GETTER_PROXY)  # 每五分钟爬取一次代理入库

    # 2.调度验证代理模块
    def verify_proxy(self):
        while True:
            verify_thread_pool()
            time.sleep(VERIFY_PROXY)

    # 3.调度api服务模块
    def api_sever(self):
        app.run()

    def run(self):
        # 调度这三个函数一起去执行,每一个函数都当做独立个体
        getter_proxy = multiprocessing.Process(target=self.getter_proxy)
        getter_proxy.start()

        if client.count() > 0:   # 数据库有代理才进行检测
            verify_proxy = multiprocessing.Process(target=self.getter_proxy)
            verify_proxy.start()

        api_sever = multiprocessing.Process(target=self.getter_proxy)
        api_sever.start()

if __name__ == '__main__':
    work = Schedule()
    work.run()