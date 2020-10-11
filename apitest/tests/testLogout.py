# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import unittest

from apitest.common.configHttp import ConfigHttp
from config import global_config


class TestLogout(unittest.TestCase):

    def setUp(self) -> None:
        self.user_token = global_config.getToken()

    def test_Logout(self):
        '''
        退出
        :return:
        '''
        payload = {
            "user_token": self.user_token

        }
        # # 推出登录
        res = ConfigHttp(uri="/loginOut", method="post", data=payload).request().json()

        self.assertEqual(res['status'], "success")
