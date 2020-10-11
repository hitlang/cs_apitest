# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
import xlrd
import os
class get_xls(object):
    def __init__(self, xls_name, sheetname):
        self.xls_name = xls_name
        self.sheetname = sheetname
        self.xlsfilepath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'testfiles', self.xls_name))

    # 获取索引
    @property
    def getsheet(self):
        workbook = xlrd.open_workbook(self.xlsfilepath)
        sheetname = workbook.sheet_by_name(self.sheetname)
        return sheetname

    # 获取所有行
    @property
    def getrows(self):
        rows = self.getsheet.nrows
        return rows

    # 获取所有列
    @property
    def getclos(self):
        cols = self.getsheet.ncols
        return cols

    @property
    def get_rows(self):
        rows = []
        rowNum = self.getsheet.nrows
        rowlist = self.getsheet.row_values
        for i in range(rowNum):
            if rowlist(i)[0] != u'case_name':
                rows.append(rowlist(i))
        return rows


'''
#--------test-------
if __name__=="__main__":
    excel=get_xls('Testcase for interface.xlsx','book_id',5)
    print(excel)
#    id_xls=excel.get_rows
    id_xls=excel.getmethod
    url=excel.geturl
    print(id_xls,url)
'''
