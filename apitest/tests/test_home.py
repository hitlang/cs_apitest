#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import os
import unittest
from apitest.common.configHttp import ConfigHttp
from apitest.params.params import HomePage


class TestHome(unittest.TestCase):

    def test_home_page(self):
        params = HomePage()
        configHttp = ConfigHttp(url=params.url[0],method="get", headers=params.headers[0])
        res = configHttp.request()
        print(res.text)
        pass

    pass