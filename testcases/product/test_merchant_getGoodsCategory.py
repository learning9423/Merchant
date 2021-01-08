import unittest
from pip._vendor import requests

from common.read_excel import ReadExcel
from common.send_request import SendRequest

getGoodsCategory_data=ReadExcel().readExcel(r'../data/getGoodsCategory_api.xlsx','Sheet1')
s = requests.session()
class GetGoodsCategory(unittest.TestCase):
    '''获取最新分类id信息'''

    def test_getGoodsCategory1(self):
        '''token正确'''
        r=SendRequest.sendRequest(s,getGoodsCategory_data[0])
        expect_result=getGoodsCategory_data[0]['expect_result'].split(":",1)[1]
        self.assertEqual(r.json()['execute_status'],eval(expect_result),msg=r.json())

    def test_getGoodsCategory2(self):
        '''token不正确'''
        r=SendRequest.sendRequest(s,getGoodsCategory_data[1])
        expect_result=getGoodsCategory_data[1]['expect_result'].split(":",1)[1]
        self.assertEqual(r.json(),eval(expect_result),msg=r.json())


if __name__ == '__main__':
    GetGoodsCategory().test_getGoodsCategory2()