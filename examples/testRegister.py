# -*-coding:utf-8 -*-
# !/usr/bin/python3
import unittest
import requests

from apitest.common.log import Log


class TestRegister(unittest.TestCase):
    url = "http://116.85.42.10:9000/register"

    def test_register_1(self):
        '''
        冒烟用例
        :return:
        '''
        payload = {
            "registerName": "kevin",
            "password": "123",
            "gender": "1"
        }

        res = requests.post(url=self.url, data=payload).json()

        self.assertEqual(res['msg'], '注册成功', "注册冒烟用例没有通过")

    def test_register_2(self):
        logger = Log()

        logger.getLogger().info("--start ----")
        '''
        回归
        :return:
        '''
        payload = {
            "registerName": "kevin",
            "password": "123",
            "gender": "1"
        }

        res = requests.post(url=self.url, data=payload).json()

        self.assertEqual(res['性别'], '男', "注册冒烟用例没有通过")

        logger.getLogger().info("---end  ----")
