import unittest



# 用例套件 方式 1
from cs_apitest.apitest.common import HTMLTestRunner
from cs_apitest.examples.testLogin import TestLogin


def smokeSuit():
    suit = unittest.TestSuite()
    suit.addTest(TestLogin("testLogin_1"))  # 加入了正向用例
    return suit


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)

    fp = open("test_report.html", "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=1, title="测试报告", description="描述")

    runner.run(smokeSuit())


