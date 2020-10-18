# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
from config import global_config
import requests
from apitest.common.log import MyLog
config = global_config


class ConfigHttp():
    def __init__(self, *, method, uri, params=None, data=None, headers=None) -> None:
        self.scheme = config.getHttpConf("scheme")
        self.baseurl = config.getHttpConf("baseurl")
        self.timeout = config.getHttpConf("timeout")
        self.apikey = config.getApikey()
        self.url = "{scheme}://{baseurl}{uri}{apikey}" \
            .format(scheme=self.scheme,
                    baseurl=self.baseurl,
                    uri=uri,
                    apikey="?apikey=" + self.apikey if self.apikey else "")
        self.params = params
        self.headers = headers
        self.data = data
        self.method = method

    def request(self):

        if self.method.upper() == 'GET':
            '''
                   发送get 请求
                   :return: 响应对象
                   '''
            try:
                response = requests.get(url=self.url, params=self.params, headers=self.headers,
                                        timeout=float(self.timeout))
                return response
            except TimeoutError:
                MyLog.get_log().error("timeout")
                pass
        elif self.method.upper() == 'POST':
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

        elif self.method.upper() == 'POSTWITHJSON':
            try:
                response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(self.timeout))
                return response
            except TimeoutError:
                MyLog.get_log().error("Time out!")
                pass

        return response


if __name__ == '__main__':
    pass
