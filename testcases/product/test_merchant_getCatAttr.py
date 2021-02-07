import unittest

from pip._vendor import requests

from common.read_excel import ReadExcel
from common.send_request import SendRequest


getCatAttr_data=ReadExcel().readExcel(r'../data/getCatAttr_api.xlsx','Sheet1')
s=requests.session()
class GetCatAttr(unittest.TestCase):
    '''查询指定分类属性接口'''

    def test_getCatAttr1(self):
        '''分类id正确，token正确'''
        r=SendRequest.sendRequest(s,getCatAttr_data[0])
        expect_result=getCatAttr_data[0]['expect_result'].split(":",1)[1]
        msg=getCatAttr_data[0]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'],eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['message'],eval(msg),msg=r.json())

    def test_getCatAttr2(self):
        '''分类id为空，token正确'''
        r=SendRequest.sendRequest(s,getCatAttr_data[1])
        expect_result=getCatAttr_data[1]['expect_result'].split(":",1)[1]
        msg=getCatAttr_data[1]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'],eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['message'],eval(msg),msg=r.json())

    def test_getCatAttr3(self):
        '''分类id错误，token正确'''
        r=SendRequest.sendRequest(s,getCatAttr_data[2])
        expect_result=getCatAttr_data[2]['expect_result'].split(":",1)[1]
        msg=getCatAttr_data[2]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'],eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['message'],eval(msg),msg=r.json())

    def test_getCatAttr4(self):
        '''分类id正确，token错误'''
        r=SendRequest.sendRequest(s,getCatAttr_data[3])
        expect_result=getCatAttr_data[3]['expect_result'].split(":",1)[1]

        self.assertEqual(r.json(),eval(expect_result),msg=r.json())

if __name__ == '__main__':
    GetCatAttr().test_getCatAttr4()