# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
线下支付流程
'''
import unittest

from apitest.api import pay_gateway
from apitest.common.configHttp import ConfigHttp
from config import global_config

from unittest.mock import Mock, patch


class TestPayment(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # global  addCartHttp
        cls.addCartHttp = ConfigHttp(uri="/addCart", method="post")
        cls.saveAddressHttp = ConfigHttp(uri="/saveAddress", method="post")
        cls.addressListHttp = ConfigHttp(uri="/addressList", method="post")
        cls.stepHttp = ConfigHttp(uri="/step", method="post")
        cls.cartSubmitHttp = ConfigHttp(uri="/cartSubmit", method="post")
        cls.orderPayFinishHttp = ConfigHttp(uri="/orderPayFinish", method="post")

    def test_add_product_cart(self):
        '''

        :return:
        '''
        # given
        user_token = global_config.getToken()
        payload = {
            "class_id": 1,
            "goods_id": 1,
            "buy_goods_num": 1,
            "user_unionid": 1,
            "user_token": user_token
        }
        self.addCartHttp.data = payload
        # when

        res = self.addCartHttp.request().json()

        # then

        self.assertEqual(res["status"], "success", "添加商品到购物车失败")
        # out
        pass

    def test_save_ship_address(self):
        # given
        user_token = global_config.getToken()
        payload = {
            "user_token": user_token,
            "true_name": "刘浪",
            "region_id": "1",
            "region_value": "北京市",
            "address": "测试地址",
            "zip_code": "1",
            "mod_phone": "13349948796",

        }
        # when
        self.saveAddressHttp.data = payload
        res = self.saveAddressHttp.request().json()
        # then
        self.assertEqual(res["status"], "success", "添加邮寄地址失败")
        pass

    def test_get_ship_address(self):
        # # given
        user_token = global_config.getToken()
        payload = {
            "user_token": user_token,

        }
        # when
        self.addressListHttp.data = payload
        res = self.addressListHttp.request().json()
        # then

        self.assertEqual(res["status"], "success", "获取配送地址失败")

        # out
        global addr_id
        addr_id = res["result"][0]["address_id"]
        pass

    def test_order_confirm(self):
        # given
        global addr_id
        user_token = global_config.getToken()
        payload = {
            "user_token": user_token,
            "address_id": addr_id,
            "user_unionid": 1
        }
        # when
        self.stepHttp.data = payload
        res = self.stepHttp.request().json()
        # then
        self.assertEqual(res["status"], "success", "订单确认失败")
        pass

    def test_sumbmit_order(self):
        # given
        global addr_id
        user_token = global_config.getToken()
        payload = {
            "user_unionid": "1",
            "address_id": addr_id,
            "user_token": user_token,
            "payment_code": "xxzf",
            "express_id": "7"
        }

        # when
        self.cartSubmitHttp.data = payload

        res = self.cartSubmitHttp.request().json()
        # then
        self.assertEqual(res["status"], "success", "提交订单失败")

        # out
        global order_id

        order_id = res["result"]["order_id"]

        pass
    @patch("apitest.api.pay_gateway.get_orderPayFinish")
    def test_order_payment(self,mock):
        # given
        global order_id
        user_token = global_config.getToken()
        payload = {
            "user_token": user_token,
            "order_id": order_id
        }
        # # when
        self.orderPayFinishHttp.data = payload

        # pay_gateway.get_orderPayFinish = Mock(return_value={"status": "fdsafds", "msg": "hahahah！"})
        mock.return_value = {"status": "success", "msg": "hahahah！"}
        res = pay_gateway.get_orderPayFinish(self.orderPayFinishHttp)
        print(res)
        # then
        self.assertEqual(res["status"], "success", "支付凭据提交失败")

        pass
