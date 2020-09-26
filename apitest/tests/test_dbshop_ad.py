# -*- coding: utf-8 -*-
# @Time : 2020/9/25 20:07
# @Author : zl
# @File : test_dbshop_ad.py
# @Software: PyCharm

import unittest
import requests
import json
import paramunittest

from apitest.common.log import Log
from config import global_config

@paramunittest.parametrized(

    {"paramName":"ad_code","testdata":""},
    {"paramName":"ad_code1","testdata":""},
    {"paramName":"","testdata":""}
)



class Test_ad_api(unittest.TestCase):



    uri = "/specialAd"
    def setUp(self) -> None:

        scheme = global_config.getHttpConf("scheme")
        baseurl =  global_config.getHttpConf("baseurl")
        self.url = scheme  + '://' + baseurl + self.uri
        self.apikey = global_config.getApikey()
        self.logger = Log.getLogger()
        self.logger.info("广告调用标记接口测试用例 开始执行")

    def setParameters(self,paramName,testdata):
        self.paramName = paramName
        self.testdata = testdata


    # def test_get_ad(self):#获取广告
    #     self.logger.info("开始执行广告接口测试用例")
    #     parma = {
    #         "ad_code":"example0",
    #         "apikey": self.apikey
    #     }
    #     res = requests.get(url=self.url, params=parma)
    #     result = res.json()
    #     self.logger.debug("调试信息2")
    #     self.assertEqual(200, res.status_code, "接口连接失败")
    #     self.assertEqual(result["status"], "success", "连接失败")
    #     self.assertEqual(result["msg"], "信息调用成功！", "广告获取失败")
    #     self.assertEqual(result["result"]["dbapi_ad_url"],"https://www.baidu.com","广告获取不正确")
    #     self.logger.info("广告接口测试用例执行结束")

    def test_ad2(self):#测试用数据驱动
        self.logger.info("开始执行广告接口异常测试用例")
        parma = {
            self.paramName:self.testdata,
            "apikey": self.apikey
        }
        res = requests.get(url=self.url,params=parma)
        result = res.json()
        self.assertFalse(result["result"])
        # self.assertEqual(200, res.status_code, "接口连接失败")
        # self.assertEqual(result["status"], "success", "连接失败")
        # self.assertEqual(result["result"], "[]", "广告获取失败")


    def tearDown(self) -> None:
        self.logger.info("广告调用标记接口测试用例 执行结束")


if __name__ == '__main__':
    unittest.main(verbosity=2)