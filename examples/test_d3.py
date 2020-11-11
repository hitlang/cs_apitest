#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import unittest


class NumbersTest(unittest.TestCase):



    def setUp(self) -> None:
        print("-------开始执行测试 -----------")

    def tearDown(self) -> None:
        print("-------结束测试 -----------")

    @classmethod
    def setUpClass(cls) -> None:
        print("==========================stetupclass===================")

    @classmethod
    def tearDownClass(cls) -> None:
        print("==========================teardown class===================")

    def test_even1(self):
        print("test_enven1111")
        self.assertEqual(1, 1)
        """
        Test that numbers between 0 and 5 are all even.
        """
        # for i in range(0, 6):
        #     with self.subTest(i=i):
        #         print("第{}".format(i))
        #         self.assertEqual(i % 2, 0)

        pass

    def test_even2(self):
        print("test_enven222")
        self.assertEqual(1, 1)
        """
        Test that numbers between 0 and 5 are all even.
        """
        # for i in range(0, 6):
        #     with self.subTest(i=i):
        #         print("第{}".format(i))
        #         self.assertEqual(i % 2, 0)

        pass