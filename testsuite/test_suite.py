import unittest
from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
import time
class test_suite(unittest.TestCase):
    def add_case(self):
        suite=unittest.TestSuite()
        spath=r'F:\jgliwork\unittest\testcases'
        suite.addTests(unittest.defaultTestLoader.discover(spath,pattern='test*.py'))
        return suite


    def run_test(self):

        now=time.time()
        rpath=r'F:\jgliwork\unittest\report\商家后台接口测试'+str(now)+'report.html'
        with open(rpath,'wb+') as f:
            runner=HTMLTestRunner(stream=f,title='商家后台测试报告',description='测试',verbosity=2)
            return runner.run(test_suite().add_case())


if __name__ == '__main__':
    test_suite().run_test()



