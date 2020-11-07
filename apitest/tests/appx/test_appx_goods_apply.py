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
                                     AppxGoodsAdd.datas[0], AppxGoodsAdd.headers[0]
        # 增加商品
        headers.update({
            "Authorization": self.config.getToken()
        })

        res = ConfigHttp(method=method, url=url, data=data, headers=headers).request().json()
        # out
        self.goods_id = res['data']  # 商品id

        self.log.debug("商品id : {}".format(self.goods_id))



    def test_apply_goods(self):
        '''
        下架商品
        :return:
        '''


        url , method , headers = AppxGoodsApply.urls[0], \
                                 AppxGoodsApply.methods[0],\
                                 AppxGoodsApply.headers[0]

        headers.update({
            "Authorization": self.config.getToken()
        })
        #
        data ={
            "ids": [self.goods_id]
        }

        res = ConfigHttp(method=method, url=url, data=data, headers=headers).request().json()

        self.log.debug("下架商品 响应数据 : {}".format(res) )

        # then
        self.assertEqual(res["code"], "000000")
        self.assertEqual(res["comment"], "Completed successfully")

        pass




