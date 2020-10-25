#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

import unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import IntegralConvertMoney
from config import global_config


class TestIntegralConvertMoney(unittest.TestCase):




    def setUp(self) -> None:
        self.log = MyLog().get_log()
        self.config = global_config



    def test_convert_success(self):


        '''
         积分转换成功的测试用例
        :return:
        '''
        #given

        user_token = self.config.getToken()
        self.log.debug("user_token ==  {}".format(user_token))
        icm = IntegralConvertMoney()

        method = icm.methods[0]
        url = icm.urls[0]
        data = icm.datas[0]
        self.log.debug("data ==  {}".format(data))

        data.update({"user_token" : user_token})


        #when

        res = ConfigHttp(method =method, url = url , data=data).request().json()

        #then

        expected = icm.expecteds[0]
        actual = res["result"]["money"]

        self.assertEqual(expected, actual, "积分转换金额失败")

        #out

        pass



