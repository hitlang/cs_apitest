# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
调用api内置广告接口测试
'''
import unittest
import paramunittest
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
@paramunittest.parametrized(
    {"pramsname": "ad_code", "testdata": ""},
    {"pramsname": "ad_error", "testdata": ""},
    {"pramsname": "", "testdata": ""},
)
class TestAd(unittest.TestCase):
    uri = "/specialAd"

    def setParameters(self, pramsname, testdata):
        '''
        :param pramsname: 参数名
        :param pramsvalue: 参数值
        :return:
        '''
        self.pramsname = pramsname
        self.testdata = testdata

    def test_345(self):


        '''
        参数化
        :return:
        '''
        params = {
            self.pramsname: self.testdata
        }

        res = ConfigHttp(uri=self.uri, params=params).get().json()

        # Log().getLogger().debug(res)
        MyLog.get_log().debug(res) #修正
        self.assertFalse(res['result'])
        pass

    def tearDown(self) -> None:
        MyLog.get_log().info("广告调用标记接口测试用例 结束执行")


if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass
