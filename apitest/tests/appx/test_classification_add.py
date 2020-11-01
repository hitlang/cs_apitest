#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import AppxClassAdd
from config import global_config


class TestClassificationAdd(unittest.TestCase):


    def setUp(self) -> None:
        aca = AppxClassAdd()
        self.url = aca.urls[0]
        self.data = aca.datas[0]
        self.headers = aca.headers[0]
        self.method = aca.methods[0]
        self.log = MyLog.get_log()
        self.config = global_config
        pass

    def test_class_add_smoke(self):
        self.headers.update({
            "Authorization": self.config.getToken()

        })

        res = ConfigHttp(method=self.method, url=self.url,  data=self.data, headers=self.headers).request().json()

        self.log.debug("class add res ==={}".format(res))

        #then

        self.assertEqual(res["code"] , "000000")
        self.assertEqual(res["comment"] , "Completed successfully")
        pass
