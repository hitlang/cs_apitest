# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import requests
import unittest
import  re

class TestAddAddress(unittest.TestCase):



    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()



    def test_1(self):
        url = "http://localhost/dbshop/user/login"


        # res = requests.get(url=url)

        res = self.session.get(url=url)


        pattern  = re.compile(r"name=\"login_security\" value=\"(.+)\" />")

        match = pattern.search(res.text)

        global  security_code


        security_code = match.group(1).strip()




        pass

    def test_2(self):
        global  security_code

        url = "http://localhost/dbshop/user/login"

        payload = {
            "user_name": "test1",
            "user_password": "123456",
            "login_security": security_code,


        }

        # res = requests.post(url=url,data=payload)

        res = self.session.post(url=url,data=payload)
        print("请求头部 ==", res.request.headers)
        print("登录响应 ==" , res.text)
        pass

    #
    def test_3(self):
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.session.close()

