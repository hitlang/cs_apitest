#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import  unittest

from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import AppxGoodsAdd
from config import global_config


class TestAppxGoodsAdd(unittest.TestCase):



    def setUp(self) -> None:
        aga  = AppxGoodsAdd()
        self.url = aga.urls[0]
        self.data = aga.datas[0]
        self.method = aga.methods[0]
        self.headers = aga.headers[0]
        self.log = MyLog.get_log()
        self.config = global_config


    def test_add_goods(self):
        '''
        增加商品冒烟用例
        :return:
        '''
        #given
        self.headers.update({
            "Authorization": self.config.getToken()

        })
        #when
        res = ConfigHttp(method=self.method, url=self.url, data=self.data, headers=self.headers).request().json()

        self.log.debug("add good json res  ==={}".format(res))
        #then
        self.assertEqual(res["code"], "000000")
        self.assertEqual(res["comment"], "Completed successfully")
        #out

        pass

    def tearDown(self) -> None:
        pass

