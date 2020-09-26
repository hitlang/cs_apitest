#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import requests
from requests.auth import HTTPBasicAuth
import unittest
class TestBasicAuth(unittest.TestCase):

    def test1(self):
        res = requests.get('http://localhost:9000/login', auth=HTTPBasicAuth('test', '123456'))

        print(res.text)

        pass

    def test2(self):
        res = requests.get('http://localhost:9000/index', auth=HTTPBasicAuth('test', '123456'))

        print(res.text)

        pass

    pass