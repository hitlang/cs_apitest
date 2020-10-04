#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
测试api没有apikey
'''
import unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog


class TestUsers(unittest.TestCase):



    def setUp(self) -> None:
        MyLog.get_log().info("--------------开始------------------------")

        self.configHttp =  ConfigHttp(uri="/users")

    def test_01(self):

        response = self.configHttp.get()

        print(response.text)
        pass

    def tearDown(self) -> None:
        MyLog.get_log().info("--------------结束--------------------")


