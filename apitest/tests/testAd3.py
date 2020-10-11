# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
调用api内置广告接口测试
ddt数据驱动
'''

import unittest
from ddt import ddt, data, unpack
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog


@ddt
class TestAd3(unittest.TestCase):
    def setUp(self) -> None:
        MyLog.get_log().info("-----------广告接口测试开始-------------------")
        self.configHttp = ConfigHttp(uri="/specialAd", method="get")
        pass

    @data({"pramsname": "ad_code", "testdata": ""},
          {"pramsname": "ad_error", "testdata": ""},
          {"pramsname": "", "testdata": ""}, )
    @unpack
    def test_Ad(self, pramsname,testdata):
        params = {
            pramsname :testdata
        }
        self.configHttp.params = params

        res = self.configHttp.request().json()

        self.assertFalse(res['result'])


    def tearDown(self) -> None:
        MyLog.get_log().info("-----------广告调用标记接口测试用例 结束执行---------------")
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass
