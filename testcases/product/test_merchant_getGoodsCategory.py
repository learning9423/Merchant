import unittest
from pip._vendor import requests

from common.read_excel import ReadExcel
from common.send_request import SendRequest


class GetGoodsCategory(unittest.TestCase):
    '''获取最新分类id信息'''
    def __init__(self):
        self.getGoodsCategory_data=ReadExcel().readExcel(r'../../data/getGoodsCategory_api.xlsx','Sheet1')
        self.s = requests.session()
        self._type_equality_funcs={}

    def test_getGoodsCategory1(self):
        '''token正确'''
        r=SendRequest.sendRequest(self.s,self.getGoodsCategory_data[0])
        expect_result=self.getGoodsCategory_data[0]['expect_result'].split(":")[1]
        self.assertEqual(r.json()['execute_status'],eval(expect_result),msg=r.json())

    def test_getGoodsCategory2(self):
        '''token不正确'''
        r=SendRequest.sendRequest(self.s,self.getGoodsCategory_data[1])
        expect_result=self.getGoodsCategory_data[1]['expect_result'].split(":")[1]
        self.assertEqual(r.json(),eval(expect_result),msg=r.json())


if __name__ == '__main__':
    GetGoodsCategory().test_getGoodsCategory2()