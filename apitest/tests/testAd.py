# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
import json
import requests
import paramunittest

from apitest.common.log import Log

'''
调用api内置广告接口测试
'''
from config import global_config


@paramunittest.parametrized(
    {"pramsname": "ad_code", "testdata": ""},

    {"pramsname": "ad_error", "testdata": ""},

    {"pramsname": "", "testdata": ""},

)
class TestAd(unittest.TestCase):
    uri = "/specialAd"

    def setUp(self) -> None:
        Log.getLogger().info("广告调用标记接口测试用例 开始执行")
        scheme = global_config.getHttpConf("scheme")
        baseurl = global_config.getHttpConf("baseurl")
        self.url = scheme + '://' + baseurl + self.uri
        self.apikey = global_config.getApikey()

    def setParameters(self, pramsname, testdata):
        '''
        :param pramsname: 参数名
        :param pramsvalue: 参数值
        :return:
        '''
        self.pramsname = pramsname
        self.testdata = testdata

    def test_345(self):
        '''
        参数化
        :return:
        '''
        params = {
             self.pramsname: self.testdata,
            "apikey": "ded63ea2d7bfc17264b83931b9045014"
        }
        print(params)
        res = requests.get(url=self.url, params=params).json()
        self.assertFalse(res['result'])
        pass

    def tearDown(self) -> None:
        Log.getLogger().info("广告调用标记接口测试用例 结束执行")


if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass
