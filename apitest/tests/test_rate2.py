# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
from unittest.mock import Mock, patch

from apitest.api.calculator import Result


class TestRate2(unittest.TestCase):

    @patch("apitest.api.calculator.Rate")
    def test_2(self , mock_object):
        x = mock_object.return_value
        x.get_rate.return_value = 2

        test_data = 1
        result  = Result()

        r = result.get_rmb(test_data)

        self.assertEqual(r, 2)

        mock_object.assert_called_once_with()
        # pass

    pass
