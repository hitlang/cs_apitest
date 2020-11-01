# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import configparser
import os

config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.ini"))


class Config:

    def __init__(self) -> None:
        self.cf = configparser.ConfigParser()  # 第一步
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

    def getDataDir(self):
        value = self.cf.get("DATA_PATH", "data_dir_path")
        return value

    def getToken(self):
        return self.cf.get("TOKEN", "user_token")

    def setToken(self, value):
        self.cf.set("TOKEN", "user_token", value)
        with open(config_file,"w") as fp:
            self.cf.write(fp)

    def setCookie(self, value):
        '''

        :param value:  cookie，格式key=value
        :return:
        '''
        self.cf.set("COOKIE", "cookie", value)
        with open(config_file,"w") as fp:
            self.cf.write(fp)

    def getCookie(self):
        return self.cf.get("COOKIE", "cookie")



# 配置对象
global_config = Config()
# test
if __name__ == '__main__':
    cf = Config()
    # port = cf.getMysqlConf("port")
    # print(port)
    cf.setCookie("sessionid=abc")

    value = cf.getCookie()

    print(value)



    pass
