import unittest
from service.calculate import *
# from BeautifulReport import BeautifulReport as bf

class TestCalculate(unittest.TestCase):

    def test_add(self):
       self.assertEqual(Calculate().add(),5)

    def test_minus(self):
        self.assertEqual(Calculate().minus(),-1)

    def test_multi(self):
        self.assertEqual(Calculate().multi(),6)

    def test_divide(self):
        self.assertEqual(Calculate().divide(),1)

# if __name__ == '__main__':
#
#     suite=unittest.TestSuite()
#
#     suite.addTest(TestCalculate('test_add'))
#     suite.addTest(TestCalculate('test_divide'))
#     run=bf(suite)
#     run.report(filename='商家后台接口测试报告',description='计算')
#     # runner=unittest.TextTestRunner()
#     # runner.run(suite)
