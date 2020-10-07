# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
关联
'''
import unittest
from ddt import ddt, data, unpack
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog

# @unittest.skip("")
@ddt
class TestGoodsInfo(unittest.TestCase):

    def setUp(self) -> None:
        # 登录
        configHttp = ConfigHttp(uri="/login")
        payload = {
            "user_name": "test1",
            "user_password": "123456"
        }
        configHttp.data = payload
        res = configHttp.post().json()

        self.assertEqual(res['status'], "success")
        globals()['user_token'] = res['result']['user_token']  # 可以使用self, 测业务流程使用globals

        self.configHttp = ConfigHttp(uri="/goodsInfo")

        pass

    # def test_1(self):
    #     global user_token
    #     MyLog.get_log().debug("获取用户登录token====" + user_token)
    #     payload = {
    #         "class_id": 1,
    #         "goods_id": 1,
    #         "user_token": user_token
    #
    #     }
    #
    #     # MyLog.get_log().debug("请求数据====" + payload)
    #     self.configHttp.data = payload
    #     res = self.configHttp.post().json()
    #     self.assertEqual(res['status'], "success")
    #     pass
    @data({
        "class_id": 1,
        "goods_id": 1,

    })
    @unpack
    def test_2(self, class_id, goods_id):
        '''
        使用ddt把测试数据抽离
        :param class_id:
        :param goods_id:
        :return:
        '''
        global user_token
        MyLog.get_log().debug("获取用户登录token====" + user_token)
        payload = {
            "class_id": class_id,
            "goods_id": goods_id,
            "user_token": user_token

        }

        # MyLog.get_log().debug("请求数据====" + payload)
        self.configHttp.data = payload
        res = self.configHttp.post().json()
        self.assertEqual(res['status'], "success")
        pass

    def tearDown(self) -> None:
        # 推出登录
        ch = ConfigHttp(uri="/loginOut")
        global user_token
        ch.data = {
            "user_token": user_token

        }
        res = ch.post().json()
        self.assertEqual(res['status'], "success")
        # self.assertEqual(res['status'], "xxx") #注意讲解

        pass
