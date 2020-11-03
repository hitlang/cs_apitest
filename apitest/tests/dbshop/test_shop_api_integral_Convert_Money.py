# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import requests
import unittest
from ddt import ddt, file_data
from apitest.common.log import MyLog
from config import global_config


@ddt
class TestIntegralConvertMoney(unittest.TestCase):

    def setUp(self) -> None:
        self.url = "http://localhost/dbshop/Jsonapi/integralConvertMoney"
        self.config = global_config

        self.log = MyLog.get_log()
        pass

    @file_data(r"E:\cs_apitest\cs_apitest\apitest\data\integral_convert_money.json")
    def test_pos_1(self, apikey, integral_num, cart_integral_num, exptected):
        # given

        params = {
            "apikey": apikey
        }

        payload = {
            "integral_num": integral_num,
            "cart_integral_num": cart_integral_num
        }

        payload.update({

            "user_token": self.config.getToken()
        })

        self.log.debug("res payload ============{}".format(payload))

        # when
        res = requests.post(self.url, params=params, data=payload).json()

        # then

        self.assertEqual(res['result']["money"], exptected, "积分转换金额不正确")

        # out

        pass

    # def test_neg_1(self):
    #     params = {
    #         "apikey": "ded63ea2d7bfc17264b83931b9045014"
    #     }
    #
    #     payload = {
    #         "integral_num": "10000",
    #         "cart_integral_num": "100"
    #     }
    #
    #     payload.update({
    #
    #         "user_token": self.config.getToken()
    #     })
    #
    #     # when
    #     res = requests.post(self.url, params=params, data=payload).json()
    #
    #     # then
    #
    #     self.assertEqual(res['result']["money"], 0, "积分转换金额不正确")

    def tearDown(self) -> None:
        pass
