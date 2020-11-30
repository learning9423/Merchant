import unittest
import requests
from common.read_excel import ReadExcel
from common.send_request import SendRequest

loginOut_data=ReadExcel().readExcel(r'../data/login_api.xlsx','Sheet2')
s=requests.session()
class LoginOut(unittest.TestCase):
    '''商家登出'''

    def test_login_out(self):
        '''商家后台退出'''
        r=SendRequest.sendRequest(s,loginOut_data[0])
        expect_result=loginOut_data[0]['expect_result'].split(":")

        self.assertEqual(r.url,eval(expect_result[1]+':'+expect_result[2]),msg=r.url)


if __name__ == '__main__':
    LoginOut().test_login_out()
