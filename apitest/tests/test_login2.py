# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
import requests
import re
from apitest.common.log import MyLog
from apitest.params.params import PcLogin
from config import global_config


class TestLogin2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.s = requests.Session()
        cls.log = MyLog.get_log()
        cls.PcLogin = PcLogin()
        cls.base_url = global_config.getHttpConf("scheme") + "://" + global_config.getHttpConf("baseurl")
        cls.log.debug("base_url == {}".format(cls.base_url))

    def test_click_login_link(self):
        headers = self.PcLogin.headers[0]
        url = self.base_url + self.PcLogin.urls[0]
        res = self.s.get(url=url, headers=headers)
        reg = re.compile(r"<input type=\"hidden\" name=\"login_security\" value=\"(.+-.+)\" />")
        match = reg.search(res.text)
        # out
        TestLogin2.security_code = match.group(1)
        self.log.debug("code  ======= {}".format(self.security_code))
        pass

    # @unittest.skip("")
    def test_login_success(self):
        # given
        url = self.base_url + self.PcLogin.urls[1]
        data = self.PcLogin.datas[1]
        data.update({"login_security": TestLogin2.security_code})
        self.log.debug("payload ========={}".format(data))
        # when
        res = self.s.post(url=url, data=data)
        reg = re.compile("退出")
        match = reg.search(res.text)
        self.assertIsNotNone(match)
        TestLogin2.log.debug(match.group())
        # out
        cookie = res.request.headers

        self.log.debug("cookie == {}".format(cookie))


        global_config.setCookie(cookie["Cookie"])
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.s.close()
        #
        pass
