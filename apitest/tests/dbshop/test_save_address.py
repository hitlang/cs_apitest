#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

import unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import SaveAddress
from config import global_config


class TestSaveAddress(unittest.TestCase):




    def setUp(self) -> None:
        self.saveAddress = SaveAddress()
        self.config = global_config
        self.log = MyLog.get_log()



    def test_add_address(self):
        '''
        增加配送地址
        :return:
        '''
        #given
        url, method, data = self.saveAddress.urls[0], self.saveAddress.methods[0], self.saveAddress.datas[0]

        user_token  = self.config.getToken()
        data.update({
            "user_token": user_token

        })
        self.configHttp = ConfigHttp(method=method, url=url, data=data)

        #when

        res = self.configHttp.request().json()

        self.log.debug("res ============{}".format(res))
        #then

        self.assertEqual("success", res["status"],"增加配送地址不成功")


        #out
        pass

    def tearDown(self) -> None:
        super().tearDown()

