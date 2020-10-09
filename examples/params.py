# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
"""
定义所有测试数据
"""
from examples import tools



def get_parameter(name):
    data = tools.GetPages.get_page_list()
    param = data[name]
    return param

class Dbshop_Info:
    params = get_parameter('Dbshop_info')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])

#test
if __name__ == '__main__':
    di = Dbshop_Info()
    print(di.data)

    pass