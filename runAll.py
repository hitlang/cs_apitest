import os
import unittest

# 用例套件 方式 1
from apitest.common import HTMLTestRunner
# from examples.testLogin import TestLogin
from apitest.tests.testLogin import TestLogin
from examples.testRegister import TestRegister


#缺点： 过于繁琐
def smokeSuite():
    suit = unittest.TestSuite()
    suit.addTest(TestLogin("testLogin_1"))
    # suit.addTest(TestRegister("test_register_1"))
    return suit
#多个套件，组成一个测试套件
def suite():
    suite1 =  unittest.makeSuite(TestLogin, "test")
    # suite2 =  unittest.makeSuite(TestRegister)

    tests = (suite1,)

    return unittest.TestSuite(tests=tests) # 这里注意讲解



if __name__ == '__main__':
    report_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"report","report.html"))
    # runner = unittest.TextTestRunner(verbosity=2) 不使用这种方式
    #
    fp = open(report_path, "wb")
    #
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="测试报告", description="描述")
    #
    # runner.run(smokeSuite()) # 1

    runner.run(suite()) # 2


