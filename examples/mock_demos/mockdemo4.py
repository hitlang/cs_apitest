# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest

from unittest.mock import Mock


class Cal():

    def add(self, x, y):
        # return x + y

        pass

    pass

class TestAdd(unittest.TestCase):
    def test_1(self):
        c = Cal()
        c.add = Mock(return_value=10)
        self.assertEqual(c.add(1, 2), 10)

        print(c.add.called)

        c.add.assert_called_with(1, 2) #检查是否被正确调用

        pass

    pass
