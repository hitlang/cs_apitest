# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import DeleteAddress
from config import global_config


class TestDeleteAddress(unittest.TestCase):

    def setUp(self) -> None:
        self.da = DeleteAddress()
        self.config = global_config
        self.log = MyLog.get_log()

    def test_get_address_id(self):
        '''
               删除配送地址
               :return:
               '''
        # given
        url, method = self.da.urls[0], self.da.methods[0]

        user_token = self.config.getToken()

        data = {
            "user_token": user_token

        }
        self.configHttp = ConfigHttp(method=method, url=url, data=data)

        # when

        res = self.configHttp.request().json()

        self.log.debug(" test_get_address_id res  ============{}".format(res))
        # then

        self.assertEqual("success", res["status"], "获取配送地址失败")

        # out
        global address_id

        address_id = res["result"][-1]["address_id"]

        self.log.debug("获取的配送地址id = {}".format(address_id))

        pass


    def test_delete_address(self):
        '''
        删除配送地址
        :return:
        '''
        # given
        url, method = self.da.urls[1], self.da.methods[1]

        user_token = self.config.getToken()
        global address_id
        data = {}
        data.update({
            "user_token": user_token,
            "address_id": address_id
        })

        self.log.debug("data request ==================  ============{}".format(data))

        self.configHttp = ConfigHttp(method=method, url=url, data=data)

        # when

        res = self.configHttp.request().json()

        self.log.debug("test_delete_address res  ============{}".format(res))
        # then

        self.assertEqual("success", res["status"], "配送地址删除不成功")

        # out
        pass

    def tearDown(self) -> None:
        super().tearDown()
