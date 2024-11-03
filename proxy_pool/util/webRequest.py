import random
import requests
from lxml import etree
from requests import Response
from settings import UA_LIST


class WebRequest(object):
    def __init__(self):
        self.response = Response()

    @property
    def user_agent(self):
        return random.choice(UA_LIST)

    @property
    def header(self):
        """请求头转为items"""
        return {'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Accept-Language': 'zh-CN,zh;q=0.8'
        }

    def get(self, url, timeout = 5):
            headers = self.header
            self.response = requests.get(url,headers=headers,timeout=timeout)
            return self

    @property
    def tree(self):
        return etree.HTML(self.response.text)
