# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import DbshopApiLogin, DbshopApiLogout


class TestApiLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.dal = DbshopApiLogin()
        self.logout = DbshopApiLogout()
        self.log = MyLog.get_log()


    def test_login_success(self):
        '''
        正向用例
        :return:
        '''
        # given

        url, method, data ,expected = self.dal.urls[0], self.dal.methods[0], self.dal.datas[0],self.dal.expecteds[0]



        # when

        res = ConfigHttp(method=method, url=url, data=data).request().json()

        self.log.debug("test_login_success 响应结果=={}".format(res))

        # then
        self.assertEqual(expected, res["status"], "登录失败")

        # out

        #退出

        url, method = self.logout.urls[0] , self.logout.methods[0]

        data  = {

            "user_token" : res["result"]["user_token"]

        }

        res = ConfigHttp(method = method, url = url, data=data).request().json()
        #


        self.assertEqual("xxxxx" , res['status'] , "退出系统失败")


        pass


