# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
积分转换金额

'''
import unittest

from ddt import ddt, file_data, unpack
import os
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import ConvertMoney
from config import global_config

test_data_file =  os.path.abspath( os.path.join(os.path.dirname(__file__) , os.pardir , "data", "test_convert_money.json"))



@ddt
class TestConvertMoney(unittest.TestCase):

    def setUp(self) -> None:
        self.log = MyLog.get_log()

    @file_data(test_data_file)
    def test_integral_convert_money(self, integral_num,cart_integral_num,expected):
        self.log.debug("{},{},{}".format(integral_num,cart_integral_num,expected))
        user_token = global_config.getToken()
        self.log.debug(user_token)
        # # given
        params = ConvertMoney()
        payload = params.data[0]
        payload.update({
            "integral_num":integral_num,
            "cart_integral_num":cart_integral_num
        })
        payload.update({"user_token" : user_token})
        self.log.debug("payload {}".format(payload))
        #  when
        confighttp = ConfigHttp(method="post", url=params.url[0], data=payload, headers=params.headers[0])
        # then
        res = confighttp.request().json()
        self.assertEqual(res["result"]["money"], expected, "积分转换金额失败")
        # out

        pass
