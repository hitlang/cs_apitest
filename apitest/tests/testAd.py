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
from config import global_config

class TestAd(unittest.TestCase):

    uri = "/specialAd"

    def setUp(self) -> None:
        Log.getLogger().info("广告调用标记接口测试用例 开始执行")
        scheme = global_config.getHttpConf("scheme")
        baseurl = global_config.getHttpConf("baseurl")
        self.url = scheme + '://' + baseurl + self.uri
        self.apikey = global_config.getApikey()


    def testAd_1(self):
        Log.getLogger().info("测试用例1.开始执行")
        # 测试数据
        test_data = "efg"
        params = {
            "ad_code": test_data,
            "apikey": "ded63ea2d7bfc17264b83931b9045014"

        }
        Log.getLogger().debug("任何的调试信息")

        res = requests.get(url=self.url, params=params).json()
        expected = "{\"status\": \"success\", \"msg\": \"信息调用成功！\",\"result\": null}"
        expected = json.loads(expected)
        self.assertDictEqual(expected, res)
        Log.getLogger().info("测试用例1.执行结束")

    def testAd_2(self):
        # 测试数据
        test_data = "example1"
        params = {
            "ad_code": test_data,
            "apikey": "ded63ea2d7bfc17264b83931b9045014"
        }

        res = requests.get(url=self.url, params=params).json()
        result = res.get('result')
        self.assertIn("test", result['dbapi_ad_body'])

    def tearDown(self) -> None:
        Log.getLogger().info("广告调用标记接口测试用例 结束执行")
