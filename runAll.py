import os
import unittest

# 用例套件 方式 1
from apitest.common import HTMLTestRunner
from examples.testLogin import TestLogin
from examples.testRegister import TestRegister
from examples.testabc import TestUsers


def smokeSuit():
    suit = unittest.TestSuite()
    suit.addTest(TestLogin("testLogin_1"))  # 加入了正向用例
    suit.addTest(TestUsers("test_users"))
    suit.addTest(TestRegister("test_register_1"))

    return suit


if __name__ == '__main__':
    report_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"report","report.html"))
    runner = unittest.TextTestRunner(verbosity=2)
    #
    fp = open(report_path, "wb")
    #
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=1, title="测试报告", description="描述")
    #
    runner.run(smokeSuit())

    print(report_path)
