# 定义接口自动化测试的关键字类
import requests

'''

'''


class KeyDemo:
    # 定义get请求方法
    def get(self, url, headers=None, param=None):
        return requests.get(url=url, headers=headers, params=param)

    # 定义post请求方法
    def post(self, url, headers=None, param=None):
        return requests.post(url=url, headers=headers, data=param)

    # 定义校验字段方法
