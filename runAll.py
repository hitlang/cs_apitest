import os
import unittest

# 用例套件 方式 1
from apitest.common import HTMLTestRunner
# from examples.testLogin import TestLogin
from apitest.tests.testGoodsInfo import TestGoodsInfo
from apitest.tests.testLogin import TestLogin
from apitest.ut.core import _TestCase
# from examples.testRegister import TestRegister


# #缺点： 过于繁琐
# def smokeSuite():
#     suit = unittest.TestSuite()
#     suit.addTest(TestLogin("testLogin_1"))
#     # suit.addTest(TestRegister("test_register_1"))
#     return suit
# 多个套件，组成一个测试套件



def suite1():
    suite = unittest.TestSuite()

    cases = [TestLogin("testLogin_1"), TestGoodsInfo("test_2")]

    suite.addTests(cases)
    return suite


#
# def suite2():
#     suite = unittest.TestSuite()
#     cases = [TestLogin("testLogin_1"), TestLogin("testLogin_2")]
#     suite.addTests(cases)
#     return suite
#
# def suite():
#     suite1 = unittest.makeSuite(TestLogin, "test")
#     suite2 = unittest.makeSuite(TestConn)
#     suite3 = unittest.makeSuite(TestShopInfo)
#     tests = (suite1, suite2, suite3)
#     return unittest.TestSuite(tests=tests)  # 这里注意讲解


if __name__ == '__main__':
    #test_data.init_data()  # 初始化接口测试数据
    # 增加
    unittest.TestCase = _TestCase
    # 测试报告
    report_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "report", "report.html"))

    fp = open(report_path, "wb")

    testcase_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "apitest", "tests"))
    #
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="测试报告", description="描述")

    discover = unittest.defaultTestLoader.discover(start_dir=testcase_path, pattern='testGoodsInfo.py')
    #
    # runner.run(smokeSuite()) # 1
    runner.run(discover)  # 2

    fp.close()
