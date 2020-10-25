# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import unittest

import requests
import re

from apitest.common.log import MyLog


class TestLogin2(unittest.TestCase):

    def setUp(self) -> None:
        # given
        url = 'http://localhost/dbshop/user/login'

        # when
        res = requests.get(url=url)

        # then
        # MyLog.get_log().debug("res ======= {}".format(res))

        reg = re.compile(r"<input type=\"hidden\" name=\"login_security\" value=\"(.+-.+)\" />")

        match = reg.search(res.text)

        # out
        self.security_code = match.group(1)
        self.cookies = res.cookies
        self.log =  MyLog.get_log()

        self.log.debug("code  ======= {}".format(self.security_code))

        pass

    def test_login_success(self):
        # given

        url = r"http://localhost/dbshop/user/login"

        payload = {
            "user_name": "test1",

            "user_password":"123456",

            "login_security":self.security_code,

            "http_referer":"http://localhost/dbshop/"

        }

        # when

        res = requests.post(url=url, data=payload, cookies =self.cookies)

        # then


        self.log.debug(res.text)

        # self.assertIn("退出",res.text, '登录失败')

        reg = re.compile("退出")

        match = reg.search(res.text)

        self.assertIsNotNone(match)


        self.log.debug(match.group())


        # out
        pass
