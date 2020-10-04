# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
from config import global_config
import requests
from apitest.common.log import MyLog
config = global_config
class ConfigHttp():
    def __init__(self, *, uri, params={}, data={}, headers={}) -> None:
        '''
        :param uri:  接口 uri
        :param params: 接口查询串
        :param data:   数据
        :param headers: 头部数据
        '''
        scheme = config.getHttpConf("scheme")
        baseurl = config.getHttpConf("baseurl")
        self.timeout = config.getHttpConf("timeout")
        apikey = config.getApikey()
        self.url = "{scheme}://{baseurl}{uri}{apikey}" \
            .format(scheme=scheme, baseurl=baseurl, uri=uri, apikey="?apikey=" + apikey if apikey else "")
        # Log().getLogger().debug(self.url)
        MyLog.get_log().debug(self.url)
        self.params = params
        self.headers = headers
        self.data = data

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

    def postWithJson(self):
        '''
        发送json数据
        :return:
        '''
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(self.timeout))
            return response
        except TimeoutError:
            MyLog.get_log().error("Time out!")

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
