# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import unittest

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
        pass

    def test_upload_personal_img(self):
        # given
        cookie = self.config.getCookie().strip() # 字符串

        value = cookie.split("=")

        # self.log.debug("cookie ===============str === {}".format(cookie))

        self.cookie = { value[0]: value[1]}

        # self.log.debug("cookie from config  == {} type == {}".format(self.cookie , type(self.cookie)))

        self.data.update(self.cookie)
        # when
        self.log.debug("date  == {}".format(self.data))
        # then



        # out

        pass

    def tearDown(self) -> None:
        super().tearDown()
