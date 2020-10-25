# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
import requests
import re
from apitest.common.log import MyLog

class TestLogin2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.s = requests.Session()

    def test_click_login_link(self):
        url = 'http://localhost/dbshop/user/login'

        res = self.s.get(url=url)
        reg = re.compile(r"<input type=\"hidden\" name=\"login_security\" value=\"(.+-.+)\" />")
        match = reg.search(res.text)
        # out
        self.security_code = match.group(1)
        self.log = MyLog.get_log()
        self.log.debug("code  ======= {}".format(self.security_code))
        pass

    def test_login_success(self):
        # given
        url = r"http://localhost/dbshop/user/login"
        payload = {
            "user_name": "test1",
            "user_password": "123456",
            "login_security": self.security_code,
            "http_referer": "http://localhost/dbshop/"
        }

        # when
        res = self.s.post(url=url, data=payload)
        reg = re.compile("退出")
        match = reg.search(res.text)
        self.assertIsNotNone(match)
        self.log.debug(match.group())

        # out
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.s.close()
