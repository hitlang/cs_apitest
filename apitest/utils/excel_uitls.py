# -*- coding: utf-8 -*-
# @Author  : lang
import os
import openpyxl

class ExcelUtil():

    def __init__(self, sheetName) -> None:
        wb = openpyxl.load_workbook(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "test_data","test_data.xlsx")))
        self.sheet = wb[sheetName]


    def get_dict(self):
        cells = self.sheet["A1":"C1"][0]
        keys = [i.value for i in cells]
        max_row = self.sheet.max_row
        end = "C{}".format(max_row)
        data_cells = self.sheet["A2":end]
        ret = []
        for r in data_cells:
            m = zip(keys, r)
            data_dict = {}
            for k, v in m:
                data_dict[k] = v.value
                pass
            ret.append(data_dict)
        return ret


if __name__ == '__main__':
    excel = ExcelUtil("正向用例")
    r = excel.get_dict()
    print(r)

