# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import AppxLogin
from config import global_config


class TestAppxLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.appxLogin = AppxLogin()
        cls.log = MyLog.get_log()
        cls.config = global_config
        pass

    def test_user_login_token(self):
        # given
        url = self.appxLogin.urls[0]
        method = self.appxLogin.methods[0]
        headers = self.appxLogin.headers[0]
        data = self.appxLogin.datas[0]
        # when
        res = ConfigHttp(method=method, url=url, data=data, headers=headers).request().json()

        # then
        self.assertEqual(res["code"], "000000", "登录获取token失败")
        # out
        global appid, token

        appid = res["data"]["apps"][0]["appId"]

        self.log.debug("appid == {}".format(appid))

        token = res["data"]["token"]

        self.log.debug("token == {}".format(token))
        pass

    def test_user_login(self):
        global token, appid
        # given
        url = self.appxLogin.urls[1]
        method = self.appxLogin.methods[1]
        headers = self.appxLogin.headers[1]

        headers.update({
            "appid": appid,

            "Authorization": token

        })

        params = {
            "appId": appid
        }

        # when
        res = ConfigHttp(method=method, params=params, url=url, headers=headers).request().json()

        self.log.debug("res === {}".format(res))

        #then
        self.assertEqual(res["code"],"000000", "重新获取token失败")

        #out
        self.config.setToken(res["data"]["token"])



        pass
