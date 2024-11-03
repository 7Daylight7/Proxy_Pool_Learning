"""
    数据库模块，提供了后续数据库操作的所有方法
"""
import random
import redis
from settings import REDIS_HOST,REDIS_PORT,REDIS_DATABASE,REDIS_OBJECT
from settings import INIT_SCORE,HIGH_SCORE,MINIMUM_SCORE,CHANGE_SCORE

class RedisClient:
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DATABASE):
        """初始化redis客户端"""
        self.db = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def exists(self,proxy):
        """判断传入的代理有没有存储到数据库"""
        # 传入的代理如果在数据库中有，则返回True，否则返回False
        return not self.db.zscore(REDIS_OBJECT,proxy) is None

    def add(self, proxy, score=INIT_SCORE):
        """添加代理到数据库，设置初始分数为10分"""
        if not self.exists(proxy):  # 如果数据库中无该代理
            print("---代理写入数据库---",proxy)
            return self.db.zadd(REDIS_OBJECT,{proxy:score})
        else:
            print("---该代理已存在---",proxy)

    def random(self):
        """随机选择一个代理"""
        proxies = self.db.zrangebyscore(REDIS_OBJECT,MINIMUM_SCORE,HIGH_SCORE)
        if len(proxies):
            return random.choice(proxies)
        else:
            print("-----数据库为空-----")  # 如果取不到可用代理

    def decrease(self,proxy):
        """传入一个代理，如果检测不过关，降低代理分数"""
        self.db.zincrby(REDIS_OBJECT,CHANGE_SCORE,proxy)  # 检测不过关就扣2分
        score = self.db.zscore(REDIS_OBJECT,proxy)
        if score <= 0:
            self.db.zrem(REDIS_OBJECT,proxy)  # 删除不可用代理

    def max(self,proxy):
        """如果检测代理可用，那么将该代理设置为最大分"""
        return self.db.zadd(REDIS_OBJECT,{proxy:HIGH_SCORE})

    def count(self):
        """当前数据库中有的代理数量"""
        return self.db.zcard(REDIS_OBJECT)

    def all(self):
        """获取所有代理，返回列表"""
        proxies = self.db.zrangebyscore(REDIS_OBJECT,MINIMUM_SCORE,HIGH_SCORE)
        if proxies:
            return proxies
        else:
            print("-----数据库为空-----")

    def count_for_num(self,number):
        """获取指定数量的代理，返回列表"""
        all_proxies = self.all()
        proxies = random.sample(all_proxies,k=number)
        return proxies


if __name__ == '__main__':
    client = RedisClient()
    # client.add()