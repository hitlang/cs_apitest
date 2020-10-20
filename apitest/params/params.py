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

    pprint(data)
    param = data[name]
    return param

class HomePage:
    params = _getParameter('homepage')
    url = []
    data = []
    headers = []
    for i in range(0, len(params)):
        url.append(params[i]["test"]["request"].get("url"))
        data.append(params[i]["test"]["request"].get("data"))
        headers.append(params[i]["test"]["request"].get("headers"))

if __name__ == '__main__':
    HomePage() #加载一次
    pass
