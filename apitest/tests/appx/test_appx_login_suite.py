#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import  unittest

from ddt import ddt, file_data

from apitest.api.login_fixture import get_user_access_token, appx_logout

@ddt
class TestAppxLoginSuite(unittest.TestCase):


    @file_data(r"E:\cs_apitest\cs_apitest\apitest\data\appx_login_data.json")
    def test_multi_login(self, phoneNumber, password):
        access_token = get_user_access_token(phoneNumber, password)
        appx_logout(access_token)
