# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
关联
'''
import unittest
from apitest.common.configHttp import ConfigHttp
class TestGoodsInfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("-------------------执行了setupclass-------------------")
        global goods_http, user_token
        payload = {
            "user_name": "test1",
            "user_password": "123456"
        }
        login_http = ConfigHttp(uri="/login", method='post', data=payload)

        res = login_http.request().json()
        user_token = res['result']['user_token']

        goods_http = ConfigHttp(uri="/goodsInfo", method="post")

    def setUp(self) -> None:
        pass

    def test_1(self):
        global goods_http, user_token

        payload = {
            "class_id": 1,
            "goods_id": 1,
            "user_token": user_token

        }
        goods_http.data = payload
        res = goods_http.request().json()
        self.assertEqual(res['status'], "success")
        pass

    def test_2(self):
        global goods_http, user_token
        payload = {
            "class_id": 1,
            "goods_id": 1,
            "user_token": user_token

        }
        goods_http.data = payload
        res = goods_http.request().json()
        self.assertEqual(res['status'], "success")
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        payload = {
            "user_token": user_token

        }
        # # 推出登录
        res = ConfigHttp(uri="/loginOut", method="post", data=payload).request().json()


        cls.assertEqual(res['status'] , "success")

