# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
单元测试
'''


def get_rmb(rmb):
    rate = get_rate()
    return rate * rmb


def get_rate():
    pass



class Result:

    def get_rmb(self, rmb):

        rate = Rate().get_rate()

        return rate * rmb



class Rate:

    def get_rate(self):
        pass