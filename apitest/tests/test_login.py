# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog

from config import global_config


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        MyLog.get_log().info("----------------登录测试开始-------------------------")
        pass

    def test_Login_success(self):
        # given
        payload = {"user_name": "test1", "user_password": "123456"}

        # when
        configHttp = ConfigHttp(url="/login", method='post', data=payload)
        res = configHttp.request().json()

        # then
        self.assertEqual("success", res['status'], "登录测试没有通过")

        # out
        user_token = res['result']['user_token']
        global_config.setToken(user_token)

    def tearDown(self) -> None:
        MyLog.get_log().info("----------------登录测试结束-------------------------")
