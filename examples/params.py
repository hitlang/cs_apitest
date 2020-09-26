# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午11:32
# @Author  : maxiang
# @File    : datas.py

"""
定义所有测试数据
"""
from examples import tools


def get_parameter(name):
    data = tools.GetPages.get_page_list()
    param = data[name]
    return param


class Basic:
    params = get_parameter('User_info')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class Tuling_Login:
    params = get_parameter('Login_info')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class Dbshop_Info:
    params = get_parameter('Dbshop_info')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class JsonPlace_Info:
    params = get_parameter('JsonPlace_info')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])

if __name__ == '__main__':
    Dbshop_Info()
    # Basic()
    pass