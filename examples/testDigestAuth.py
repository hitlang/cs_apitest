#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import requests
from requests.auth import HTTPDigestAuth
import unittest
class TestDigestAuth(unittest.TestCase):

    def test1(self):
        res = requests.get('http://localhost:9000/login2', auth=HTTPDigestAuth('test', '123456'))

        print(res.text)

        pass



    pass