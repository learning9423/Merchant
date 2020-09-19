import unittest
import requests

from common.read_excel import ReadExcel
from common.send_request import SendRequest


class LoginOut(unittest.TestCase):
    '''商家登出'''
    def __init__(self):
        #数据初始化
        self.loginOut_data=ReadExcel().readExcel(r'../data/login_api.xlsx','Sheet2')
        self.s=requests.session()
        self._type_equality_funcs={}
        
    def test_login_out(self):
        '''商家后台退出'''
        r=SendRequest.sendRequest(self.s,self.loginOut_data[0])
        expect_result=self.loginOut_data[0]['expect_result'].split(":")

        self.assertEqual(r.url,eval(expect_result[1]+':'+expect_result[2]),msg=r.url)


if __name__ == '__main__':
    LoginOut().test_login_out()
