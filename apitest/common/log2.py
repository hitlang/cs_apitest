# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import logging
from typing import Any


class Log2():
    _instance = None

    def __new__(cls) -> Any:
        if  cls._instance is None:
            cls._instance = object.__new__(cls)
            return cls._instance
        else:

            return cls._instance

    def __init__(self) -> None:
        print("开始调用")
        # create logger
        self.logger = logging.getLogger('simple_example')
        self.logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # add formatter to ch
        ch.setFormatter(formatter)
        # add ch to logger
        self.logger.addHandler(ch)

    @classmethod
    def getLogger(cls):
        if cls._instance is None:
            cls._instance = Log2()
        return cls._instance

global_logger = Log2()
    # 'application' code
    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warning('warn message')
    # logger.error('error message')
    # logger.critical('critical message')
#test
if __name__ == '__main__':
    # Log2().logger.debug("debug message")

    log2 = Log2.getLogger()
    log3 = Log2.getLogger()

    print(id(log2))
    print(id(log3))
    pass
