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
    return param #是测试用例的列表

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
    params = _getParameter('pc_login')
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

class UploadImg:
    '''

    '''
    params = _getParameter('upload_img')
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

class AppxLogin:
    params = _getParameter('appx_login')
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

class AppxLogout:
    params = _getParameter('appx_logout')
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

class AppxClassAdd:
    params = _getParameter('appx_class_add')
    urls = []
    datas = []
    headers = []
    names = []
    methods = []
    expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        headers.append(params[i]["test"]["request"].get("headers"))
        methods.append(params[i]["test"]["request"].get("method"))
        expecteds.append(params[i]["test"]["request"].get("expected"))
        names.append(params[i]["test"].get("name"))

class SaveAddress:
    params = _getParameter('save_address')
    urls = []
    datas = []
    headers = []
    names = []
    methods = []
    expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        headers.append(params[i]["test"]["request"].get("headers"))
        methods.append(params[i]["test"]["request"].get("method"))
        expecteds.append(params[i]["test"]["request"].get("expected"))
        names.append(params[i]["test"].get("name"))

class DeleteAddress:
    params = _getParameter('delete_address')
    urls = []
    datas = []
    headers = []
    names = []
    methods = []
    expecteds = []
    for i in range(0, len(params)):
        urls.append(params[i]["test"]["request"].get("url"))
        datas.append(params[i]["test"]["request"].get("data"))
        headers.append(params[i]["test"]["request"].get("headers"))
        methods.append(params[i]["test"]["request"].get("method"))
        expecteds.append(params[i]["test"]["request"].get("expected"))
        names.append(params[i]["test"].get("name"))
if __name__ == '__main__':
    icm = DeleteAddress()
    print(icm.datas[1])
    print(icm.urls[1])
    print(icm.methods[1])
    print(icm.names[1])
    print(icm.headers[1])



    pass