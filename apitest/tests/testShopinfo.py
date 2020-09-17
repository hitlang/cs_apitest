# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang


import unittest
import requests

from apitest.config.config import Config

cf  = Config()

class TestShopInfo(unittest.TestCase):

    url = "shopinfo"

    def setUp(self) -> None:
        global  cf
        scheme = cf.getHttpConf("scheme")
        baseurl = cf.getHttpConf("baseurl")
        self.apikey = cf.getApikey()
        self.url  = scheme + "://" + baseurl +  "/" + TestShopInfo.url


        # self.url = "http://localhost/dbshop/Jsonapi/shopinfo"
        #
        # self.apikey = "ded63ea2d7bfc17264b83931b9045014"



    # @unittest.skip("")
    def test_1(self):
        '''
        冒烟用例
        :return:
        '''
        params = {

            "apikey": self.apikey
        }
        res = requests.get(url=self.url, params=params).json()

        self.assertEqual("success", res['status'])



    def tearDown(self) -> None:
        print("test over")

