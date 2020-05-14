import unittest
from service.calculate import *

class TestCalculate(unittest.TestCase):

    def test_add(self):
       self.assertEqual(Calculate().add(),5)

    def test_minus(self):
        self.assertEqual(Calculate().minus(),-1)

    def test_multi(self):
        self.assertEqual(Calculate().multi(),6)

    def test_divide(self):
        self.assertEqual(Calculate().divide(),0)

if __name__ == '__main__':

    suite=unittest.TestSuite()

    suite.addTests(TestCalculate('test_add'))

    unittest.TextTestRunner().run(suite)