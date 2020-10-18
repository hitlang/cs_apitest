# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
from unittest.mock import Mock, patch

from apitest.api import calculator
from apitest.api.calculator import get_rmb


class TestRate(unittest.TestCase):

    # def test_1(self):
    #     x = 1
    #
    #     calculator.get_rate = Mock(return_value = 2)
    #
    #     y = get_rmb(x)
    #     self.assertEqual(y, 2)
    #
    #     calculator.get_rate.assert_called_once_with()
    #     pass

    @patch("apitest.api.calculator.get_rate")
    def test_2(self , mock_object):
        x = 1

        # calculator.get_rate = Mock(return_value=2)
        mock_object.return_value = 2
        y = get_rmb(x)
        self.assertEqual(y, 2)

        mock_object.assert_called_once_with()
        pass

    pass
