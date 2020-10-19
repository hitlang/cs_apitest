# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
调用api内置广告接口测试
ddt数据驱动
'''

import os
import unittest
from ddt import ddt, data, unpack
from apitest.utils.excelUitls import ExcelUtil

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, "testfiles", "test_cases.xlsx"))
excel_data = ExcelUtil(file_path, "ad",start_col=1, end_col=2).get_dict()

@ddt
class TestAd4(unittest.TestCase):
    @data(*excel_data)
    @unpack
    def test_Ads(self, pramsname, testdata):
        print(pramsname)
        self.assertEqual(eval(testdata), "")

        pass

