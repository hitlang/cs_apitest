# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
from config import global_config
import requests
from apitest.common.log import MyLog

config = global_config


class ConfigHttp():
    def __init__(self, *, uri) -> None:
        MyLog.get_log().debug("---------创建ConfigHttp对象---------")
        scheme = config.getHttpConf("scheme")
        baseurl = config.getHttpConf("baseurl")
        self.timeout = config.getHttpConf("timeout")
        apikey = config.getApikey()
        self.url = "{scheme}://{baseurl}{uri}{apikey}" \
            .format(scheme=scheme, baseurl=baseurl, uri=uri, apikey="?apikey=" + apikey if apikey else "")
        self._params = {}
        self._headers = {}
        self._data = {}

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def get(self):
        '''
        发送get 请求
        :return: 响应对象
        '''
        try:
            response = requests.get(url=self.url, params=self.params, headers=self.headers, timeout=float(self.timeout))
            return response
        except TimeoutError:
            MyLog.get_log().error("timeout")
            pass

    def post(self):
        '''
        发送post请求
        :return:
        '''
        try:
            response = requests.post(self.url, data=self.data, headers=self.headers, timeout=float(self.timeout))
            return response
        except TimeoutError:
            MyLog.get_log().error("timeout")
            pass

    # def postWithJson(self):
    #     '''
    #     发送json数据
    #     :return:
    #     '''
    #     try:
    #         response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(self.timeout))
    #         return response
    #     except TimeoutError:
    #         MyLog.get_log().error("Time out!")
    #         pass

    # def postWithFile(self):
    #     fp = open(self.file_path, 'rb')
    #     self.files = {"filename": fp}
    #     try:
    #         response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
    #                                  timeout=float(timeout))
    #         fp.close()
    #         return response
    #     except TimeoutError:
    #         self.logger.error("Time out!")
    #         return None
    #


if __name__ == '__main__':
    pass
