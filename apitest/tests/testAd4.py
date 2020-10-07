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
from apitest.common.log import MyLog
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, "data", "test_data6.json"))
with open(file_path) as fp:
    test_data = json.load(fp)
    pass
# print(file_path)
@ddt
@unittest.skip("")
class TestAd4(unittest.TestCase):

    # @file_data(file_path)
    # def test_Ads_1(self, pramsname, testdata):
    #     MyLog.get_log().info(pramsname + "|" + testdata)
    #
    #     self.assertEqual(1, 1)
    #
    #     pass


    # @file_data(file_path)
    # def test_Ads_2(self, value):
    #     test_data = eval(value[0])
    #
    #
    #     print(test_data) #字典
    #
    #     self.assertEqual(1, 1)
    #
    #     pass


    # @file_data(file_path)
    # def test_Ads(self, pramsname,testdata):
    #     # print(pramsname, testdata)
    #     pass

    @data(*test_data)
    @unpack
    def test_Ads(self, pramsname,testdata):
        # print(pramsname, testdata)
        pass
