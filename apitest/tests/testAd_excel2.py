# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
调用api内置广告接口测试
ddt数据驱动,在进一步封装
'''

import unittest
from ddt import ddt, file_data, data, unpack
import json
import os
from pprint import pprint
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.utils.excel_uitls import ExcelUtil

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, "testfiles", "test_cases.xlsx"))
excel_data = ExcelUtil(file_path, "ad2", start_col=1, end_col=7).get_dict()


pprint(excel_data)

@ddt
class TestAd4(unittest.TestCase):

    @data(*excel_data)
    #@unpack
    def test_Ads(self, test_case):
        '''
        given
        what
        then
        :param test_case:
        :return:
        '''
        ch = ConfigHttp(method=test_case["method"],
                        uri=test_case["uri"],
                        params=eval(test_case['params']),  # 为字典
                        data=test_case['data'],
                        headers=test_case['headers'])

        res = ch.request().json()

        self.assertEqual(eval(test_case['expected']), res['result'])

        pass
