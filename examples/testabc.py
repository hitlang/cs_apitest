# -*-coding:utf-8 -*-
# !/usr/bin/python3
import unittest

import requests


class TestUsers(unittest.TestCase):
    url = "http://10.255.0.187:9000/users"

    # 第一个用例
    def test_users(self):
        res = requests.get(url=self.url).json()

        self.assertIn("吴云露", res, "用例失败 ")

        pass

    pass
