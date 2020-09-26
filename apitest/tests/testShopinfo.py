# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
import requests
from config import global_config
class TestShopInfo(unittest.TestCase):
    uri = "shopinfo"
    def setUp(self) -> None:
        scheme = global_config.getHttpConf("scheme")
        baseurl = global_config.getHttpConf("baseurl")
        self.apikey = global_config.getApikey()
        self.url = scheme + "://" + baseurl + "/" + self.uri

    def test_shopinfo_smoke(self):
        params = {
            "apikey": self.apikey
        }
        res = requests.get(url=self.url, params=params).json()
        self.assertEqual("success", res['status'])

    def tearDown(self) -> None:
        print("test over")
