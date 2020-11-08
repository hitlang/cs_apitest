# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
更新商品推荐状态
'''
import unittest
from collections import defaultdict
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import AppxGoodsAdd, AppxGoodsRecommend
import  time
from config import global_config


class TestAppxUpdateRecomm(unittest.TestCase):

    def setUp(self) -> None:
        self.log = MyLog.get_log()
        self.config = global_config


        def __add_goods():
            method, url, data, headers = AppxGoodsAdd.methods[0], \
                                         AppxGoodsAdd.urls[0], \
                                         AppxGoodsAdd.datas[0], AppxGoodsAdd.headers[0]
            # 增加商品
            headers.update({
                "Authorization": self.config.getToken()
            })

            data.update(

                {
                    "name" : "测试商品" + str(round(time.time()))
                }
            )

            res = ConfigHttp(method=method, url=url, data=data, headers=headers).request().json()
            # out
            goods_id = res['data']  # 商品id

            # self.log.debug("商品id : {}".format(goods_id))
            return goods_id

        #添加十个商品
        self.ids = [  __add_goods() for i in range(11)]

        self.log.debug("=======ids =====" + str(self.ids))




    def test_appx_goods_recomm(self):
        '''
        更新商品推荐状态
        用例1

        :return:
        '''

        url, method, headers, data = AppxGoodsRecommend.urls[0], \
                                     AppxGoodsRecommend.methods[0], \
                                     AppxGoodsRecommend.headers[0], \
                                     AppxGoodsRecommend.datas[0]

        headers.update({
            "Authorization": self.config.getToken()
        })

        data.update({

            # "ids": [self.goods_id]
            "ids": self.ids

        })
        #

        res = ConfigHttp(method=method, url=url, data=data, headers=headers).request().json()

        self.log.debug("更新商品推荐状态 响应数据 : {}".format(res))

        # then
        self.assertEqual(res["code"], "000000")
        self.assertEqual(res["comment"], "Completed successfully")

        pass
