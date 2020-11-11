#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
单元测试。测试python 核心api
'''
import yaml

import unittest

class TestStringMethods(unittest.TestCase):

    @unittest.skipIf(yaml.__version__  != "5.1.1", "版本不符合")
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FO')


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())



class Test_2(unittest.TestCase):

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)