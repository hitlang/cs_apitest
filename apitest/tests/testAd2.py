# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
import json
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog

'''
调用api内置广告接口测试
'''
from config import global_config


class TestAd(unittest.TestCase):
    uri = "/specialAd"

    def setUp(self) -> None:
        # MyLog.get_log().info("广告调用标记接口测试用例 开始执行")
        # scheme = global_config.getHttpConf("scheme")
        # baseurl = global_config.getHttpConf("baseurl")
        # self.url = scheme + '://' + baseurl + self.uri
        # self.apikey = global_config.getApikey()
        pass

    def test_Ad_1(self):
        MyLog.get_log().info("测试用例1.开始执行")
        # 测试数据
        test_data = "efg"
        params = {
            "ad_code": test_data
        }
        MyLog.get_log().debug("任何的调试信息")

        # res = requests.get(url=self.url, params=params).json()
        res = ConfigHttp(uri=self.uri,params=params).get().json()
        expected = "{\"status\": \"success\", \"msg\": \"信息调用成功！\",\"result\": null}"
        expected = json.loads(expected)
        self.assertDictEqual(expected, res)
        MyLog.get_log().info("测试用例1.执行结束")

    def test_Ad_2(self):
        # 测试数据
        test_data = "example1"
        params = {
            "ad_code": test_data,
        }

        res = ConfigHttp(uri=self.uri,params=params).get().json()
        result = res.get('result')
        self.assertIn("test", result['dbapi_ad_body'])



    def tearDown(self) -> None:
        MyLog.get_log().info("广告调用标记接口测试用例 结束执行")


if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass
