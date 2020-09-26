# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
from config import global_config
import requests

config = global_config


class Request():
    # 增加强制标记，避免出错
    def __init__(self, *, uri) -> None:
        '''
        :param url:  接口uri
        '''
        scheme = config.getHttpConf("scheme")
        baseurl = config.getHttpConf("baseurl")

        global timeout
        timeout = config.getHttpConf("timeout")
        # self.url = scheme + '://' + baseurl
        self.url = "{scheme}://{baseurl}{uri}".format(scheme=scheme, baseurl=baseurl, uri=uri)
        self.apikey = config.getApikey()
        print(self.apikey)
        self.params = {}
        self.headers = {}

        pass

    def get(self):
        '''
        发送get 请求
        :return: 响应对象
        '''
        response = requests.get(url=self.url, params=self.params, headers=self.headers, timeout=float(timeout))
        return response

    def post(self):
        try:
            response = requests.post(self.url, data=self.data, headers=self.headers, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time Out!")
            return None

    def postWithFile(self):
        fp = open(self.file_path, 'rb')
        self.files = {"filename": fp}
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                     timeout=float(timeout))
            fp.close()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def postWithJson(self):
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None


if __name__ == '__main__':
    r = Request(uri="")

    r.params = {

        "apikey": r.apikey

    }

    res = r.get()

    print(res.json())

    pass
