import unittest
from service.calculate import *
# from BeautifulReport import BeautifulReport as bf

class TestCalculate(unittest.TestCase):

    def test_add(self):
        '''测试用例1：哈哈'''
        self.assertEqual(Calculate().add(),5)

    def test_minus(self):
        self.assertEqual(Calculate().minus(),-1)

    def test_multi(self):
        self.assertEqual(Calculate().multi(),6)

    def test_divide(self):
        self.assertEqual(Calculate().divide(),1)

