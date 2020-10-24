# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import requests
import unittest
import re
''''
'''
@unittest.skip("")
class TestLoginPc(unittest.TestCase):

    def setUp(self) -> None:
        url = "http://116.85.42.10/user/login"
        res = requests.get(url=url)
        reg = re.compile(r"<input type=\"hidden\" name=\"login_security\" value=\"(.+)\" />")
        match = reg.search(res.text)
        self.cookies = res.cookies
        self.code = match.group(1)



    def test_login(self):
        # given
        data = {
            "user_name": "test1",
            "user_password": "123456",
            "http_referer": "http://116.85.42.10/user/login"

        }
        url2 = "http://116.85.42.10/user/login"
        headers = {
            "Referer": "http://116.85.42.10/user/login",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
        }

        #关联数据
        payload = {
            "login_security": self.code
        }
        payload.update(data)
        # when
        res = requests.post(url=url2, data=payload , headers=headers, cookies = self.cookies)
        #then
        self.assertIn("退出",res.text)
        pass
