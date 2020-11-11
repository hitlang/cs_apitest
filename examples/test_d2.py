#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import unittest


class Test_3(unittest.TestCase):

    def test_split3(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split("2")
    pass