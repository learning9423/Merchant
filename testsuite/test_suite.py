import logging
import time
import unittest
from HTMLTestRunner import HTMLTestRunner


class test_suite(unittest.TestCase):

    def add_case(self):
        suite=unittest.TestSuite()
        spath='../testcases'
        suite.addTests(unittest.defaultTestLoader.discover(spath,pattern='test_merchant_deleteGoods.py'))
        return suite

    def run_test(self):
        log_path='../log'
        now=time.time()
        rpath=r'../report/商家后台接口测试'+str(now)+'report.html'
        logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=log_path + '/' + str(now) + r"result.log",
                        filemode='w')
        logger = logging.getLogger()
        logger.debug(self.add_case())
        with open(rpath,'wb+') as f:
            runner=HTMLTestRunner(stream=f,title='商家后台测试报告',description='商家后台测试环境接口测试，本次测试接口为商品模块接口',verbosity=2)
            return runner.run(self.add_case())

if __name__ == '__main__':
    test_suite().run_test()



