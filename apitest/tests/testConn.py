# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
import requests

class TestConn(unittest.TestCase):

    def setUp(self) -> None:
        self.url = "http://localhost/dbshop/Jsonapi"

        self.apikey = "ded63ea2d7bfc17264b83931b9045014"

    # 测试用例1
    def test_1(self):

        params = {

            "apikey" : self.apikey
        }
        res = requests.get(url=self.url , params=params).json()



        self.assertEqual(res['status'] , "success", "接口连接失败")

    # 测试用例2
    def test_2(self):
        params = {

            "apikey": "123"
        }
        res = requests.get(url=self.url, params=params).json()

        self.assertEqual(res['status'], "error")

    def tearDown(self) -> None:
        pass
