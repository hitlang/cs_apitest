# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest
from apitest.common.configHttp import ConfigHttp
from apitest.common.log import MyLog
from apitest.params.params import UploadImg
from config import global_config


class TestUploadImg(unittest.TestCase):

    def setUp(self) -> None:
        self.config = global_config
        self.upload = UploadImg()
        self.url = self.upload.urls[0]
        self.method = self.upload.methods[0]
        self.data = self.upload.datas[0]
        self.headers = self.upload.headers[0]
        self.log = MyLog.get_log()
        self.file = open(r'E:\cs_apitest\cs_apitest\apitest\tests\test_03.jpg', 'rb')
        files = {'user_avatar': self.file}
        cookie = self.config.getCookie().strip()  # 字符串
        value = cookie.split("=")
        self.cookie = {value[0]: value[1]}
        self.confg_http = ConfigHttp(method=self.method, url=self.url, data=self.data, headers=self.headers,
                                     files=files, cookies=self.cookie)
        pass

    def test_upload_personal_img(self):
        # when
        self.log.debug("date ===== == {}".format(self.data))
        res = self.confg_http.request()

        pass

    def tearDown(self) -> None:
        self.file.close()
