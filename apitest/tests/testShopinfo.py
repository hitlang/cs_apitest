# -*-coding:utf-8 -*-
# !/usr/bin/python3


import unittest
import requests

class TestShopInfo(unittest.TestCase):


    def setUp(self) -> None:
        self.url = "http://localhost/dbshop/Jsonapi/shopinfo"

        self.apikey = "ded63ea2d7bfc17264b83931b9045014"



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

