# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
import requests

# 声明全局变量
from config import Config, global_config

localconfig = Config()
# localconfig = global_config # 注意讲解
class TestConn(unittest.TestCase):

    def setUp(self) -> None:
        global  localconfig
        scheme = localconfig.getHttpConf("scheme")
        baseurl = localconfig.getHttpConf("baseurl")
        self.url = scheme + '://' + baseurl
        self.apikey = localconfig.getApikey()


    def test_connection_error_apikey(self):
        params = {
            "apikey": "123"
        }
        res = requests.get(url=self.url, params=params).json()
        self.assertEqual(res['status'], "error")



    def test_connection_smoke(self):
        params = {
            "apikey" : self.apikey
        }
        res = requests.get(url=self.url , params=params).json()
        self.assertEqual(res['status'] , "success", "接口连接失败")


    def tearDown(self) -> None:
        pass
