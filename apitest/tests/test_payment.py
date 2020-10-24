# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
线下支付流程
'''
import os
import unittest
from apitest.api import pay_gateway
from apitest.common.configHttp import ConfigHttp
from apitest.params.params import Payment
from config import global_config

@unittest.skip("")
class TestPayment(unittest.TestCase):

    def test_add_product_cart(self):
        # given
        parmas = Payment()

        configHttp = ConfigHttp(url=parmas.url[0], method="post" , data=parmas.data[0])

        # when
        user_token = global_config.getToken()
        configHttp.data.update({"user_token": user_token})
        res = configHttp.request().json()

        # then
        self.assertEqual(res["status"], "success", "添加商品到购物车失败")
        # out
        pass

    def test_save_ship_address(self):
        # given
        parmas = Payment()
        configHttp = ConfigHttp(url=parmas.url[1], method="post",data=parmas.data[1])
        # when
        user_token = global_config.getToken()
        configHttp.data.update({"user_token": user_token})
        res = configHttp.request().json()
        # then
        self.assertEqual(res["status"], "success", "添加邮寄地址失败")
        pass
    #
    def test_get_ship_address(self):
        # given
        parmas = Payment()
        configHttp = ConfigHttp(url=parmas.url[2], method="post",data=parmas.data[2])
        # when
        user_token = global_config.getToken()
        configHttp.data.update({ "user_token": user_token})
        res = configHttp.request().json()
        # then
        self.assertEqual(res["status"], "success", "获取配送地址失败")
        # out
        global addr_id
        addr_id = res["result"][0]["address_id"]
    #
    #
    def test_order_confirm(self):
        # given
        parmas = Payment()
        configHttp = ConfigHttp(url=parmas.url[3],method="post", data=parmas.data[3])

        # when
        global addr_id
        user_token = global_config.getToken()
        configHttp.data.update({ "user_token": user_token,"address_id": addr_id})
        res = configHttp.request().json()

        # then
        self.assertEqual(res["status"], "success", "订单确认失败")
        pass
    #
    def test_sumbmit_order(self):
        # given
        parmas = Payment()
        configHttp = ConfigHttp(url=parmas.url[4], method="post", data=parmas.data[4])
        # when
        user_token = global_config.getToken()
        global addr_id
        extract = {
            "address_id": addr_id,
            "user_token": user_token
        }
        configHttp.data.update(extract)
        res = configHttp.request().json()
        # then
        self.assertEqual(res["status"], "success", "提交订单失败")

        # out
        global order_id

        order_id = res["result"]["order_id"]

        pass
    #
    # # @patch("apitest.api.pay_gateway.get_orderPayFinish")
    # def test_order_payment(self,mock = None):
    #     # given
    #     test_data = r[5]["test"]["request"]
    #     configHttp = ConfigHttp(**test_data)
    #
    #     global order_id
    #     user_token = global_config.getToken()
    #     extract = {
    #         "user_token": user_token,
    #         "order_id": order_id
    #     }
    #     # # when
    #     configHttp.data.update(extract)
    #
    #     # mock.return_value = {"status": "success", "msg": "hahahah！"}
    #
    #     res = pay_gateway.get_orderPayFinish(configHttp)
    #
    #     #then
    #     self.assertEqual(res["status"], "success", "订单完成付款失败")
    #
    #     pass
