# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import AppxLogin, AppxLogin1
from config import global_config


class TestAppxLogin1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = MyLog.get_log()
        cls.config = global_config
        pass

    def test_user_login1(self):
        # given
        url = AppxLogin1.urls[0]
        method = AppxLogin1.methods[0]
        headers = AppxLogin1.headers[0]
        data = AppxLogin1.datas[0]

        # when
        res = ConfigHttp(method=method, url=url, data=data, headers=headers).request().json()

        # then
        self.assertEqual(res["code"], "000000", "登录获取token失败")

        pass


