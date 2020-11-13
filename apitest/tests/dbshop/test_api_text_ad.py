# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
from ddt import ddt, file_data
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import DbshopApiTextAd
from config import global_config
import os
data_dir = global_config.getDataDir()

@ddt
class TestApiTextAdSuite(unittest.TestCase):

    def setUp(self) -> None:
        self.log = MyLog.get_log()

    # 第一个用例
    @file_data( os.path.join(data_dir , "dbshop_api_text_ad.json"))
    def test_api_text_ad(self, ad_code):
        '''
        正向用例
        :return:
        '''
        # given

        url, method, data  = DbshopApiTextAd.urls[0], DbshopApiTextAd.methods[0], DbshopApiTextAd.datas[0]

        data.update({

            "ad_code":ad_code

        })

        # when
        res = ConfigHttp(method=method, url=url, params=data).request().json()
        self.log.debug("test_api_text_ad 响应结果=={}".format(res))
        # then
        self.assertEqual(ad_code, res["result"]['dbapi_ad_code'], "文字广告调用标记失败")



