# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
import requests

# 声明全局变量
from config import global_config


class TestConn(unittest.TestCase):


    def setUp(self) -> None:
        scheme = global_config.getHttpConf("scheme")
        baseurl = global_config.getHttpConf("baseurl")
        self.url = scheme + '://' + baseurl
        self.apikey = global_config.getApikey()

    def test_connection_smoke(self):
        params = {
            "apikey": self.apikey
        }
        res = requests.get(url=self.url, params=params).json()
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
