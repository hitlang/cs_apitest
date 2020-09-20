import requests
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.url = "http://116.85.42.10:9000/login"

    # 冒烟测试用例
    def testLogin_01(self):
        payload = {
            "loginName": "jack",
            "password": "123"
        }

        res = requests.post(url=self.url, data=payload).json()
        self.assertEqual(res['status'], 0, "登陆测试失败")

    # 反向测试用例1_用户名有误
    def testLogin_02(self):
        payload = {
            "loginName": "jack_",
            "password": "123"
        }

        res = requests.post(url=self.url, data=payload).json()
        self.assertEqual(res['status'], -1, "登陆测试失败，用户名有误")

    # 反向测试用例2_密码有误
    def testLogin_03(self):
        payload = {
            "loginName": "jack",
            "password": "1234"
        }

        res = requests.post(url=self.url, data=payload).json()
        self.assertEqual(res['status'], -1, "登陆测试失败，密码有误")

    # 反向测试用例3_用户名_密码有误
    def testLogin_04(self):
        payload = {
            "loginName": "jack_",
            "password": "1234"
        }

        res = requests.post(url=self.url, data=payload).json()
        self.assertEqual(res['status'], -1, "登陆测试失败，用户名有误")