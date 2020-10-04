# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
调用api内置广告接口测试
'''
import json
import unittest
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog


class TestAd(unittest.TestCase):
    uri = "/specialAd"

    def setUp(self) -> None:
        pass

    def test_Ad_1(self):
        MyLog.get_log().info("测试用例1.开始执行")
        params = {
            "ad_code": "efg"
        }
        # MyLog.get_log().debug("任何的调试信息")
        res = ConfigHttp(uri=self.uri, params=params).get().json()
        expected = "{\"status\": \"success\", \"msg\": \"信息调用成功！\",\"result\": null}"
        expected = json.loads(expected)
        self.assertDictEqual(expected, res)
        MyLog.get_log().info("测试用例1.执行结束")

    def test_Ad_2(self):
        params = {
            "ad_code": "example1",
        }
        res = ConfigHttp(uri=self.uri, params=params).get().json()
        self.assertIn("test", res['result']['dbapi_ad_body'])

    def tearDown(self) -> None:
        MyLog.get_log().info("广告调用标记接口测试用例 结束执行")


if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass
