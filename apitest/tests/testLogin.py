# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog

# @unittest.skip("")
from config import global_config


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        MyLog.get_log().info("----------------登录测试开始-------------------------")
        self.configHttp = ConfigHttp(uri="/login", method='post')
        pass




    def test_Login_2(self):
        '''
        用户名错
        :return:
        '''
        payload = {
            "user_name": "test",
            "user_password": "123456"
        }
        self.configHttp.data = payload
        res = self.configHttp.request().json()
        self.assertEqual("error", res['status'], "登录测试没有通过")

    def test_Login_3(self):
        '''
        密码错误
        :return:
        '''
        payload = {
            "user_name": "test",
            "user_password": "12345"
        }
        self.configHttp.data = payload
        res = self.configHttp.request().json()
        self.assertEqual("error", res['status'], "登录测试没有通过")

    def test_Login_1(self):
        '''
        冒烟用例
        :return:
        '''
        payload = {
            "user_name": "test1",
            "user_password": "123456"
        }
        self.configHttp.data = payload
        res = self.configHttp.request().json()
        self.assertEqual("success", res['status'], "登录测试没有通过")
        user_token = res['result']['user_token']
        global_config.setToken(user_token)


    def tearDown(self) -> None:
        MyLog.get_log().info("----------------登录测试结束-------------------------")
