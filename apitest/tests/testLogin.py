# -*-coding:utf-8 -*-
# !/usr/bin/python3
import unittest
import requests

from apitest.config.config import Config
# 声明全局变量
localconfig = Config()

class TestLogin(unittest.TestCase):
    url = "login"

    def setUp(self) -> None:
        global localconfig
        scheme = localconfig.getHttpConf("scheme")
        baseurl = localconfig.getHttpConf("baseurl")
        self.url = scheme + '://' + baseurl + '/' + TestLogin.url
        #
        # self.url = "http://localhost/dbshop/Jsonapi"
        #
        # self.apikey = "ded63ea2d7bfc17264b83931b9045014"

    def testLogin_1(self):
        '''
        冒烟用例
        :return:
        '''
        payload = {
            "user_name": "test1",
            "user_password": "123456"
        }

        apikey = localconfig.getApikey()
        params = {

            "apikey": apikey
        }
        res = requests.post(url=self.url, data=payload, params=params).json()

        self.assertEqual("success", res['status'], "登录测试没有通过")

    # @unittest.skip('')
    def testLogin_2(self):
        '''
        用户名错
        :return:
        '''
        payload = {
            "user_name": "test",
            "user_password": "123456"
        }

        params = {

            "apikey": localconfig.getApikey()
        }
        res = requests.post(url=self.url, data=payload, params=params).json()

        self.assertEqual("error", res['status'], "登录测试没有通过")

    def testLogin_3(self):
        '''
        密码错误
        :return:
        '''
        payload = {
            "user_name": "test",
            "user_password": "12345"
        }

        params = {

            "apikey": localconfig.getApikey()
        }
        res = requests.post(url=self.url, data=payload, params=params).json()

        self.assertEqual("error", res['status'], "登录测试没有通过")

    # 只要setup成功执行，那么必定执行
    def tearDown(self) -> None:
        print("test over")
