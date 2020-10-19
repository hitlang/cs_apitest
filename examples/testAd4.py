# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
调用api内置广告接口测试
ddt数据驱动
'''

import unittest
from ddt import ddt, file_data, data, unpack
import json
import os
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, "data", "test_data6.json"))

@ddt
class TestAd4(unittest.TestCase):
    def setUp(self) -> None:
        MyLog.get_log().info("广告调用标记接口测试用例 开始执行")
        self.configHttp = ConfigHttp(uri="/specialAd", method="get")
    #
    @file_data(file_path)
    def test_Ads(self, pramsname,testdata):
        params = {
            pramsname: testdata
        }
        self.configHttp.params = params
        res = self.configHttp.request().json()
        MyLog.get_log().debug("-----res---" + str(res))
        self.assertFalse(res['result'])

    # @file_data(file_path)
    # def test_Ads(self, value):
    #     res = eval(value[0]) # 把json串转换为字典
    #     MyLog.get_log().info(res["pramsname"])
    #
    #
    #     # params = {
    #     #     pramsname: testdata
    #     # }
    #     # self.configHttp.params = params
    #     # res = self.configHttp.request().json()
    #     # MyLog.get_log().debug("-----res---" + str(res))
    #     # self.assertFalse(res['result'])

