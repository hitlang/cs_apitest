# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
import requests
# 声明全局变量
from apitest.common.request import Request
from config import global_config
class TestConn(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_connection_smoke(self):
        r = Request(uri="")
        params = {
            "apikey": r.apikey
        }
        r.params = params
        res = r.get().json()
        self.assertEqual(res['status'], "success", "接口连接失败")


    def test_connection_error_apikey(self):
        params = {
            "apikey": "123"
        }
        res = requests.get(url=self.url, params=params).json()
        self.assertEqual(res['status'], "error")

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)

    pass
