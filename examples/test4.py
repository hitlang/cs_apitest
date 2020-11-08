# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

from functools import wraps


def a(x):
    @wraps()
    def b():
        print(x)

    return b
