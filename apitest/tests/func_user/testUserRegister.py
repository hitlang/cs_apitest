# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import unittest

from apitest.common.log import Log


@unittest.skip("")
class TestUserRegister(unittest.TestCase):

    def setUp(self) -> None:
        Log.getLogger().info("start ")

    def test_1(self):
        self.assertEqual(1, 1)
        pass

    def tearDown(self) -> None:
        Log.getLogger().info("end")
