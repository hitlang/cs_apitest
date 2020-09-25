# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
import requests

from config import Config, global_config

# localconfig = Config()
localconfig = global_config # 注意讲解

class TestShopInfo(unittest.TestCase):
    url = "shopinfo"

    def setUp(self) -> None:
        global localconfig
        scheme = localconfig.getHttpConf("scheme")
        baseurl = localconfig.getHttpConf("baseurl")
        self.apikey = localconfig.getApikey()
        self.url = scheme + "://" + baseurl + "/" + TestShopInfo.url

    def test_shopinfo_smoke(self):
        params = {
            "apikey": self.apikey
        }
        res = requests.get(url=self.url, params=params).json()
        self.assertEqual("success", res['status'])

    def tearDown(self) -> None:
        print("test over")
