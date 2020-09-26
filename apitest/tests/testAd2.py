# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
import json
import requests
from apitest.common.log import Log
'''
调用api内置广告接口测试
'''
class TestAd(unittest.TestCase):

    def testAd_1(self):
        Log.getLogger().info("测试用例1 开始执行")

        url = "http://localhost/dbshop/Jsonapi/specialAd"
        # 测试数据
        test_data = "efg"
        params = {
            "ad_code": test_data,
            "apikey": "ded63ea2d7bfc17264b83931b9045014"

        }
        Log.getLogger().debug("任何的调试信息")

        res = requests.get(url=url, params=params).json()
        expected = "{\"status\": \"success\", \"msg\": \"信息调用成功！\",\"result\": null}"
        expected = json.loads(expected)
        self.assertDictEqual(expected, res)
        Log.getLogger().info("测试用例1.执行结束")

    def testAd_2(self):
        url = "http://localhost/dbshop/Jsonapi/specialAd"
        # 测试数据
        test_data = "example1"
        params = {
            "ad_code": test_data,
            "apikey": "ded63ea2d7bfc17264b83931b9045014"
        }

        res = requests.get(url=url, params=params).json()
        result = res.get('result')
        self.assertIn("test", result['dbapi_ad_body'])
