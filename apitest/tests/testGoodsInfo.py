# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
关联
'''
import unittest
from apitest.common.configHttp import ConfigHttp
from config import global_config


class TestGoodsInfo(unittest.TestCase):

    def setUp(self) -> None:

        self.user_token = global_config.getToken()


    def test_1(self):
        payload = {
            "class_id": 1,
            "goods_id": 1,
            "user_token": self.user_token

        }
        goods_http = ConfigHttp(uri="/goodsInfo", method="post")


        goods_http.data = payload
        res = goods_http.request().json()
        self.assertEqual(res['status'], "success")
        pass

    def test_2(self):
        # global goods_http, user_token
        # global goods_http

        payload = {
            "class_id": 1,
            "goods_id": 1,
            "user_token": self.user_token

        }
        goods_http = ConfigHttp(uri="/goodsInfo", method="post")
        goods_http.data = payload
        res = goods_http.request().json()
        self.assertEqual(res['status'], "success")
        pass



