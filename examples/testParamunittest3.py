#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import time
import unittest
import paramunittest
from apitest.utils import configxls

ReadConfigXls = configxls.get_xls('training_interfaceTestCase.xlsx','add_Groups')
login_xls = ReadConfigXls.get_rows
print(login_xls)
@paramunittest.parametrized(*login_xls)
class addGroupsTest(unittest.TestCase):
    def setParameters(self,case_name,method,token,recommend,name,sequence,logo,parentId,source,status,storeId,result,code,comment):
        self.case_name=str(case_name)
        print(self.case_name)
        self.method = str(method)
        self.token = str(token)
        self.recommend = str(recommend)
        self.name = str(name)
        self.sequence=str(sequence)
        self.logo = str(logo)
        self.parentId = str(parentId)
        self.source = str(source)
        self.status = str(status)
        self.storeId = str(storeId)
        self.result = str(result)
        self.code = str(code)
        self.comment = str(comment)
        self.response=None
        self.info = None



if __name__ == "__main__":
    unittest.main(verbosity=2)