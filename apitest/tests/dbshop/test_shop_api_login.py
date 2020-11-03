# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import unittest

import requests

from config import global_config


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.config = global_config

        pass


    def test_login_success(self):
        # given
        url = "http://localhost/dbshop/Jsonapi/login"
        payload = {
            "user_name": "test1",
            "user_password": "123456",
            "user_unionid": "1"
        }

        params = {

            "apikey": "ded63ea2d7bfc17264b83931b9045014"
        }
        # when
        res = requests.post(url, data=payload, params=params).json()

        # then

        self.assertEqual(res["status"], "success", "登录不成功")

        # out

        user_token = res["result"]["user_token"]

        # 写入全局配置文件

        self.config.setToken(user_token)

        pass
