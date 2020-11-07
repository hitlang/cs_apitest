# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
下架商品
'''
import unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import AppxGoodsApply, AppxGoodsAdd
from config import global_config


class TestAppxGoodsApply(unittest.TestCase):

    def setUp(self) -> None:
        self.log = MyLog.get_log()
        self.config = global_config
        method, url, data, headers = AppxGoodsAdd.methods[0], \
                                     AppxGoodsAdd.urls[0], \
                                     AppxGoodsAdd.datas[0], AppxGoodsAdd.datas[0]
        # 增加商品
        headers.update({
            "Authorization": self.config.getToken()
        })

        res = ConfigHttp(method=method, url=url, data=data, headers=headers).request().json()
        # out
        self.goods_id = res['data']  # 商品id

    def test_apply_goods(self):
        '''
        下架商品
        :return:
        '''
        # aga = AppxGoodsApply()
        #
        # data ={
        #     "ids": [self.goods_id]
        # }


        pass




