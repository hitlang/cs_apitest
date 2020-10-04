# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
from apitest.common.configHttp import ConfigHttp


class TestShopInfo(unittest.TestCase):
    uri = "/shopinfo"

    def setUp(self) -> None:
        pass

    def test_shopinfo_smoke(self):
        res = ConfigHttp(uri=self.uri).get().json()
        self.assertEqual("success", res['status'])

    def tearDown(self) -> None:
        print("test over")
