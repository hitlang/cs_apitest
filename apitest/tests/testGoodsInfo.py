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
        payload = {
            "user_name": "test1",
            "user_password": "123456"
        }
        # 登录
        configHttp = ConfigHttp(uri="/login", method='post', data=payload)
        res = configHttp.request().json()
        self.assertEqual(res['status'], "success")
        globals()['user_token'] = res['result']['user_token']  # 可以使用self, 测业务流程使用globals

        self.configHttp = ConfigHttp(uri="/goodsInfo", method="post")

        pass

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
        res = self.configHttp.request().json()
        self.assertEqual(res['status'], "success")
        pass

    def tearDown(self) -> None:
        global user_token
        payload = {
            "user_token": user_token

        }
        # 推出登录
        ch = ConfigHttp(uri="/loginOut", method="post", data=payload)

        res = ch.request().json()
        self.assertEqual(res['status'], "success")
        # self.assertEqual(res['status'], "xxx") #注意讲解

        pass
