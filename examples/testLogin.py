# -*-coding:utf-8 -*-
# !/usr/bin/python3


import unittest
import requests
@unittest.skip("")
class TestLogin(unittest.TestCase):

    # url = "http://localhost/dbshop/Jsonapi/login"

    # apikey = "ded63ea2d7bfc17264b83931b9045014"
    # 如果setup方法引发异常，框架认为测试遇到了错误，测试用例不执行
    def setUp(self) -> None:
        self.url = "http://localhost/dbshop/Jsonapi/login"

        self.apikey = "ded63ea2d7bfc17264b83931b9045014"



    @unittest.skip("")
    def testLogin_1(self):
        '''
        冒烟用例
        :return:
        '''
        payload = {
            "user_name": "test1",
            "user_password": "123456"
        }

        params = {

            "apikey": self.apikey
        }
        res = requests.post(url=self.url, data=payload, params=params).json()

        self.assertEqual("success", res['status'], "登录测试没有通过")

    @unittest.skip('')
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

            "apikey": self.apikey
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

            "apikey": self.apikey
        }
        res = requests.post(url=self.url, data=payload, params=params).json()



        self.assertEqual("error", res['status'], "登录测试没有通过")
    #只要setup成功执行，那么必定执行
    def tearDown(self) -> None:
        print("test over")

