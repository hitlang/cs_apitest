#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import AppxLogout
from config import global_config


class TestAppxLogout(unittest.TestCase):


    def setUp(self) -> None:
        al = AppxLogout()
        self.url = al.urls[0]
        self.method = al.methods[0]
        self.headers  = al.headers[0]
        self.log = MyLog.get_log()
        self.config = global_config

    def test_appx_logout(self):

        self.headers.update({

            "Authorization": self.config.getToken()
        })

        res = ConfigHttp(method = self.method, url= self.url, headers=self.headers).request().json()

        self.log.debug("logout res ===={}".format(res))
        pass
