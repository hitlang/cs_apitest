# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import requests
import unittest
import re
from apitest.common.log import MyLog
from apitest.params.params import PcLoginLink, PcLoginPost
''''
'''


class TestLoginPc(unittest.TestCase):

    def setUp(self) -> None:
        pll = PcLoginLink()
        self.session = requests.Session()  # 创建一个会话对象

        url = pll.url[0]

        headers = pll.headers[0]
        res = self.session.get(url=url, headers=headers)

        reg = re.compile(r"<input type=\"hidden\" name=\"login_security\" value=\"(.+)\" />")

        MyLog.get_log().debug("cookies{}".format(res.request.headers))
        match = reg.search(res.text)
        # self.cookies = res.cookies
        self.code = match.group(1)

    def test_login(self):
        plp = PcLoginPost()
        # given
        data = plp.data[0]
        url2 = plp.url[0]
        headers = plp.headers[0]

        # 关联数据
        payload = {
            "login_security": self.code
        }
        payload.update(data)
        # when
        res = self.session.post(url=url2, data=payload, headers=headers)

        MyLog.get_log().debug("response : {}".format(res.text))
        # then
        self.assertIn("退出", res.text)
        pass
