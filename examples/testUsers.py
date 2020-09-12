#-*-coding:utf-8 -*-
#!/usr/bin/python3

import unittest
import requests

class TestUsers(unittest.TestCase):




    def test_users(self):
        '''
        冒烟用例
        :return:
        '''
        # url = "http://10.255.0.187:9000/users"
        url = "http://localhost:9000/users"
        res = requests.get(url).json()
        self.assertIn("吴云露" , res)



