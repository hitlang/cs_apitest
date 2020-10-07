# __author__ = 'Daolin.Yang'
# coding=utf-8
# !/usr/bin/python
import os
import unittest
from apitest.common import HTMLTestRunner
from apitest.common.log import MyLog


class AllTest:
    def __init__(self):
        self.caseDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "apitest", "tests"))
        self.caseList = []
        pass

    def set_case_list(self):
        fb = open("caselist.txt")
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList:
            case_name = case.split("/")[-1]
            print(case_name + ".py")
            discover = unittest.defaultTestLoader.discover(self.caseDir, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            if suit is not None:
                MyLog.get_log().info("-------------------------测试开始-----------------------")

                # 测试报告
                report_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "report", "report.html"))
                fp = open(report_path, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Interface Test Report', description='饼图统计表：')
                runner.run(suit)
                fp.close()
            else:
                pass
        except Exception as ex:
            MyLog.get_log().error(str(ex))
        finally:
            MyLog.get_log().info("-------------------------测试结束-----------------------")


if __name__ == '__main__':
    at = AllTest()

    # at.set_case_list()

    at.set_case_suite()

    pass