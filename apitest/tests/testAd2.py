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
# @unittest.skip("")
class TestAd2(unittest.TestCase):
    def setUp(self) -> None:
        MyLog.get_log().info("-----------广告接口测试开始-------------------")
        # self.configHttp = ConfigHttp(uri="/specialAd")
        self.configHttp = ConfigHttp(uri="/specialAd", method="get")
        pass

    def test_Ad_1(self):
        params = {
            "ad_code": "efg"
        }
        self.configHttp.params = params

        res = self.configHttp.request().json()

        expected = "{\"status\": \"success\", \"msg\": \"信息调用成功！\",\"result\": null}"
        expected = json.loads(expected)
        self.assertDictEqual(expected, res)


    def test_Ad_2(self):
        params = {
            "ad_code": "example1",
        }
        self.configHttp.params = params

        res = self.configHttp.request().json()

        self.assertIn("test", res['result']['dbapi_ad_body'])

    def tearDown(self) -> None:
        MyLog.get_log().info("-----------广告调用标记接口测试用例 结束执行---------------")
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass
