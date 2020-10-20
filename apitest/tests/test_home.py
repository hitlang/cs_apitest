#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import os
import unittest
from apitest.common.configHttp import ConfigHttp
from apitest.common.loader import load_test_file
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, "data", "test_home.json"))
r = load_test_file(file_path)

class TestHome(unittest.TestCase):

    def test_home_page(self):
        test_data = r[0]["test"]["request"]
        configHttp = ConfigHttp(**test_data)
        res = configHttp.request()
        print(res.text)
        pass

    pass