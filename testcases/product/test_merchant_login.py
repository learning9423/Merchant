import ddt
import requests
import unittest

from common.read_excel import ReadExcel
from common.send_request import SendRequest


class TestLogin(unittest.TestCase):
    '''商家后台登录'''
    def __init__(self):
        # 数据初始化
        self.login_data = ReadExcel().readExcel(r'../data/login_api.xlsx', 'Sheet1')
        self.s = requests.session()
        self._type_equality_funcs={}

    def test_login1(self):
        '''用户名和密码都正确'''
        r = SendRequest.sendRequest(self.s, self.login_data[0])
        expect_result=self.login_data[0]['expect_result'].split(":")[1]
        msg=self.login_data[0]['msg']
        print(r.json())
        self.assertEqual(r.json()['code'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['msg'], msg, msg=r.json())

    def test_login2(self):
        '''用户名密码都错误'''
        r = SendRequest.sendRequest(self.s, self.login_data[1])
        print(r.json())
        expect_result=self.login_data[1]['expect_result'].split(":")[1]
        msg=self.login_data[1]['msg']

        self.assertEqual(r.json()['code'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['msg'], msg, msg=r.json())

    def test_login3(self):
        '''用户名正确密码错误'''
        r = SendRequest.sendRequest(self.s, self.login_data[2])
        expect_result=self.login_data[2]['expect_result'].split(":")[1]
        msg=self.login_data[2]['msg']

        self.assertEqual(r.json()['code'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['msg'], msg, msg=r.json())

    def test_login4(self):
        '''用户名错误密码正确'''
        r = SendRequest.sendRequest(self.s, self.login_data[3])
        expect_result=self.login_data[3]['expect_result'].split(":")[1]
        msg=self.login_data[3]['msg']

        self.assertEqual(r.json()['code'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['msg'], msg, msg=r.json())
    def test_login5(self):
        '''用户名密码为空'''
        r = SendRequest.sendRequest(self.s, self.login_data[4])
        expect_result=self.login_data[4]['expect_result'].split(":")[1]
        msg=self.login_data[4]['msg']

        self.assertEqual(r.json()['code'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['msg'], msg, msg=r.json())


if __name__ == '__main__':
    TestLogin().test_login1()
