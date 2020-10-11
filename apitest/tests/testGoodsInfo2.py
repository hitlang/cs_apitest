# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import unittest
import os
from pprint import pprint

from ddt import ddt, file_data, data, unpack

from apitest.common.configHttp import ConfigHttp

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, "data", "test_data_shopInfo.json"))


@ddt
class TestGoodsInfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        global configHttp
        configHttp = ConfigHttp(uri="/goodsInfo", method="post")

    @data({
        "class_id": 1,
        "goods_id": 1,

    })
    @unpack
    def test_shopInfo_smoke(self, class_id, goods_id):
        global configHttp
        payload = {
            "class_id": class_id,
            "goods_id": goods_id
        }
        configHttp.data = payload
        res = configHttp.request().json()
        self.assertEqual(res['status'], "success")
        self.assertEqual(res['result']['goods_id'], "1")

    @file_data(file_path)
    def test_goodsid_or_classid_error(self, uri, method, data, expected):
        global configHttp
        configHttp = ConfigHttp(uri=uri, method=method)
        configHttp.data = eval(data)
        res = configHttp.request().json()
        self.assertEqual(res['status'], expected)
        pass
