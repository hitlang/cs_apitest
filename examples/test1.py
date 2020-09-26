import unittest
import paramunittest

test_data = [(1, 2), (4, 5)]
@paramunittest.parametrized(
    *test_data
)
# @paramunittest.parametrized(
#     # ('1', '2'),
#     # #(4, 3),
#     # ('2', '3'),
#     # (('4', ), {'b': '5'}),
#     # {'a': 5, 'b': 6},
# )
class TestFoo(unittest.TestCase):
    def setParameters(self, a, b):
        self.a = a
        self.b = b

    def testLess(self):
        print("a==", self.a)
        print("b==", self.b)
        self.assertLess(self.a, self.b)


if __name__ == '__main__':
    unittest.main(verbosity=2)

    pass
