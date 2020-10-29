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



class IntegralConvertMoney:
    '''
    积分转换金额测试数据类
    '''
    params = _getParameter('integralConvertMoney')
    urls = []
    datas = []
    headers = []
    names= []
    methods= []
    expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        headers.append(params[i]["test"]["request"].get("headers"))
        methods.append(params[i]["test"]["request"].get("method"))
        expecteds.append(params[i]["test"]["request"].get("expected"))
        names.append(params[i]["test"].get("name"))

class PcLogin:
    '''

    '''
    params = _getParameter('pc_login_loginout')
    urls = []
    datas = []
    headers = []
    names= []
    methods= []
    expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        headers.append(params[i]["test"]["request"].get("headers"))
        methods.append(params[i]["test"]["request"].get("method"))
        expecteds.append(params[i]["test"]["request"].get("expected"))
        names.append(params[i]["test"].get("name"))


if __name__ == '__main__':
    icm = PcLogin()
    print(icm.datas[0])
    print(icm.urls[0])
    print(icm.methods[0])
    print(icm.names[0])


    pass