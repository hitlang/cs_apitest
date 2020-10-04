#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
from apitest.utils.excel_uitls import ExcelUtil

e = ExcelUtil('login')

r = e.get_dict()


print(r)


