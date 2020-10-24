#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

"""
定义所有测试数据
"""
import os
from pprint import pprint
from apitest.params import tools

path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

def _getParameter(name):
    data = tools.GetPages().get_page_list()
    # pprint(data)
    param = data[name]
    return param

class Payment:
    params = _getParameter('payment')
    url = []
    data = []
    headers = []
    names= []
    for i in range(0, len(params)):
        url.append(params[i]["test"]["request"].get("url"))
        data.append(params[i]["test"]["request"].get("data"))
        headers.append(params[i]["test"]["request"].get("headers"))
        names.append(params[i]["test"].get("name"))

class PcLoginLink:
    params = _getParameter('pc_login_link')
    url = []
    data = []
    headers = []
    names= []
    for i in range(0, len(params)):
        url.append(params[i]["test"]["request"].get("url"))
        data.append(params[i]["test"]["request"].get("data"))
        headers.append(params[i]["test"]["request"].get("headers"))
        names.append(params[i]["test"].get("name"))

class PcLoginPost:
    params = _getParameter('pc_login_post')
    url = []
    data = []
    headers = []
    names= []
    for i in range(0, len(params)):
        url.append(params[i]["test"]["request"].get("url"))
        data.append(params[i]["test"]["request"].get("data"))
        headers.append(params[i]["test"]["request"].get("headers"))
        names.append(params[i]["test"].get("name"))

class ConvertMoney:
    '''
    积分转换金额参数
    '''
    params = _getParameter('convert_money')
    url = []
    data = []
    headers = []
    names=[]
    for i in range(0, len(params)):
        url.append(params[i]["test"]["request"].get("url"))
        data.append(params[i]["test"]["request"].get("data"))
        headers.append(params[i]["test"]["request"].get("headers"))
        names.append(params[i]["test"].get("name"))

