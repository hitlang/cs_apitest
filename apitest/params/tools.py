#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
"""
使用har2case， 生成 ，读取yaml测试数据，所有。
"""
from pprint import pprint

import yaml
import os
import os.path

def parse():
    #yaml文件的目录所在路径
    path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/params/Param'
    pages = {}
    for root, dirs, files in os.walk(path_ya):
        # print("root {}, \ndirs {} , \nfiles {}\n".format(root, dirs, files))
        for name in files:
            #每个Param目录下，yaml文件的绝对路径
            watch_file_path = os.path.join(root, name)
            with open(watch_file_path, 'r',encoding='UTF-8') as f:
                page = yaml.safe_load(f)
                pages.update(page)
        return pages


class GetPages:
    @staticmethod
    def get_page_list():
        _page_list = {}
        pages = parse()

        for page, value in pages.items():
            parameters = value['parameters']
            data_list = []

            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page] = data_list

        return _page_list


if __name__ == '__main__':
    lists = GetPages.get_page_list()
    # pprint(lists)


    pass
