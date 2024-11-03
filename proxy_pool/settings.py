"""
    项目的配置文档
"""

"""数据库配置"""
REDIS_HOST = '127.0.0.1'  # 数据库所在ip地址
REDIS_PORT = 6379  # 数据库所在端口
REDIS_DATABASE = 0  # 操作哪一个数据库

REDIS_OBJECT = 'PROXIES'  # 数据库操作的对象

"""数据库分数设置"""
INIT_SCORE = 10  # 初始分数
HIGH_SCORE = 50  # 最高分数
MINIMUM_SCORE = 1  # 最低分数
HIGHEST_SCORE = 49  # 范围指定

"""减分"""
CHANGE_SCORE = -2

"""时间间隔配置"""
GETTER_PROXY = 60 * 5  # 获取代理的时间间隔
VERIFY_PROXY = 60 * 3  # 验证代理的时间间隔

"""测试超时时间"""
VERIFY_TIMEOUT = 5  # 测试代理是否可行超时时间

"""测试地址"""
VERIFY_URL = 'https://www.baidu.com/'

"""User-Agent列表"""
UA_LIST = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17720',
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.8810.3391 Safari/537.36 Edge/18.14383',
        'Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931',
        'Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
        'Mozilla/5.0 (Windows NT 6.2;WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
        ]