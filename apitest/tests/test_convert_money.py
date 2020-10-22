# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
积分转换金额

'''
import unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import ConvertMoney


class TestConvertMoney(unittest.TestCase):

    def test_integral_convert_money(self):
        # given
        params = ConvertMoney()
        confighttp = ConfigHttp(method="post", url=params.url[0], data=params.data[0], headers=params.headers[0])

        # when
        res = confighttp.request().json()

        MyLog.get_log().debug("积分转换金额响应结果" + str(res))

        # then
        self.assertEqual(res["status"], "success", "积分转换金额失败")
        # out

        pass

    pass
