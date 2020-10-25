#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

import unittest
import os
from ddt import ddt, file_data

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import IntegralConvertMoney
from config import global_config

test_json_data = os.path.abspath(os.path.join(global_config.getDataDir(),"test_convert_money.json"))
MyLog.get_log().debug("test_json_data  {}".format(test_json_data))

@ddt
class TestIntegralConvertMoney(unittest.TestCase):




    def setUp(self) -> None:
        self.log = MyLog().get_log()
        self.config = global_config


    @file_data(test_json_data)
    def test_convert_success(self,integral_num,cart_integral_num,expected):


        '''
         积分转换成功的测试用例
        :return:
        '''
        #given

        user_token = self.config.getToken()
        self.log.debug("user_token ==  {}".format(user_token))
        icm = IntegralConvertMoney()


        method, url ,data  = icm.methods[0], icm.urls[0], icm.datas[0]
        self.log.debug("data ==  {}".format(data))

        data.update({"user_token" : user_token})
        data.update({
            "integral_num" :integral_num,
            "cart_integral_num":cart_integral_num

        })


        #when

        res = ConfigHttp(method =method, url = url , data=data).request().json()

        #then

        # expected = icm.expecteds[0]

        actual = res["result"]["money"]

        self.assertEqual(expected, actual, "积分转换金额失败")

        #out

        pass



