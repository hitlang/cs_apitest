# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import os

import  pprint

import  yaml
yaml_dir_path =   os.path.abspath( os.path.join(os.path.dirname(__file__), os.pardir , "apitest", "data"))
# print(yaml_dir_path)
# os.walk(top=yaml_dir_path) # 是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)
#
def parse():
    pages = {}
    for   root, dirs , files in os.walk(top=yaml_dir_path):
        for name in files :
            watch_file_path = os.path.join(root, name)
            with open(watch_file_path , mode="rt" , encoding="utf-8") as f:
                page = yaml.safe_load(f)
                pages.update(page)
                pass
        pprint.pprint(pages)
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
    r = GetPages.get_page_list()

    pprint.pprint(r)

    # for name in dirs:
    #     print(os.path.join(root, name))

    # print(dirs)
    #
    # print(files)
    #
    # print("=====================")

    pass
