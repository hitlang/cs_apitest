# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import configparser
import os

from apitest.common.log import Log

config_file = os.path.abspath( os.path.join( os.path.dirname(__file__),"config.ini"))


class Config:

    def __init__(self) -> None:
        self.logger = Log.getLogger()
        self.logger.info("------------------创建配置对象----------------------")
        self.cf = configparser.ConfigParser() # 第一步
        self.cf.read(config_file)

    def getHttpConf(self, key):
        value = self.cf.get("HTTP", key)
        return value

    # 获取接口访问密钥
    def getApikey(self):
        return self.cf.get("APIKEY", "apikey")

    def getMysqlConf(self, key):
        value = self.cf.get("MYSQL", key)
        return value
# 配置对象
global_config = Config()
# test
if __name__ == '__main__':
    cf = Config()
    port = cf.getMysqlConf("port")
    print(port)
    pass