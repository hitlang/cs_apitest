# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import logging
import os
from typing import Any


class Log():

    __instance = None

    def __init__(self) -> None:
        # create logger
        self.logger = logging.getLogger('simple_example')
        self.logger.setLevel(logging.DEBUG)
        # 日志文件
        log_file = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, "log", "log.log"))

        # create console handler and set level to debug
        # ch = self.loggerlogging.StreamHandler()
        ch = logging.FileHandler(filename=log_file, encoding="utf-8", mode="wt")

        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        self.logger.addHandler(ch)

    def __new__(cls) -> Any:
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def getLogger(self):

        return self.logger




if __name__ == '__main__':

    myLogger =  Log()
    # myLogger2 =  Log()
    #
    # print( id(myLogger))
    # print( id(myLogger2))


    logger = myLogger.getLogger()
    # # 'application' code
    logger.debug('debug message')
    # logger.info('info message')
    # logger.warning('warn message')
    # logger.error('error message')
    # logger.critical('critical message')
    #
    # logger.debug("test abc")
    # logger.debug("中文")

    # os.path.join(os.path.dirname(__file__), os.path.pardir)
    # print( os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, "log","log.log")))

    pass
