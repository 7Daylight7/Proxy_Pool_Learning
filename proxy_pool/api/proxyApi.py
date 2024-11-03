"""
服务模块
搭建一个简易网站
编写模块(链接地址)
客户端访问这个链接，就能拿到代理数据
"""

import flask  # 是一个能够为我们提供api接口，网站开发的框架
from db.redisClient import RedisClient
from flask import request  # 获取url地址中的参数
from flask import jsonify  # 可以把对象转化为字符串

# 实例化数据库对象
client = RedisClient()

# 实例化一个app(application)对象
# __name__ 一般写法，app对象的名字
app = flask.Flask(__name__)

# 视图函数: 提供服务的接口 eg:http://118.24.52.95:5010/get/

@app.route('/')  # 将下面的函数挂载到路由
def index():
    # 视图函数返回的数据，只能返回字符串数据类型#####
    return '<h2> 欢迎来到代理池 <h2>'

@app.route('/get')
def get_proxy():
    """随机获取一个代理"""
    one_proxy = client.random()
    return one_proxy

@app.route('/getcount')
def get_any_proxy():
    """获取指定数量的代理"""
    # 拿到查询参数的值
    num = request.args.get('num','')
    # 有可能用户没有传递查询参数
    if not num :  # 如果没有获取到查询参数
        num = 1  # 没哟查询参数则默认查询1个
    else:
        num = int(num)
    any_proxy = client.count_for_num(num)
    return jsonify(any_proxy)

@app.route('/getnum')
def get_count_proxy():
    """获取所有代理的数量"""
    count_proxy = client.count()
    return f"代理池可用的数量为:{count_proxy}个"  # 代理可用的数量为

@app.route('/getall')
def get_all_proxy():
    """获取所有代理"""
    all_proxy = client.all()
    return jsonify(all_proxy)

if __name__ == '__main__':
    # 运行实例化的app对象
    app.run()
