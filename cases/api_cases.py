import configparser
import unittest
from ddt import ddt, feed_data

# 创建一个UnitTest测试用例管理框架
from api_keywords.keyword import KeyDemo


@ddt
class ApiCases(unittest.TestCase):
    # 测试用例
    def test_01_api(self):
        # 实例化
        conf = configparser.ConfigParser()
        kd = KeyDemo()
