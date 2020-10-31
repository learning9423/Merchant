import unittest
from pip._vendor import requests

from common.read_excel import ReadExcel


class GetGoodsCategory(unittest.TestCase):
    '''获取最新分类id信息'''
    def __init__(self):
        self.getGoodsCategory_data=ReadExcel().readExcel(r'../../data/getGoodsCategory_api.xlsx','Sheet1')
        print(self.getGoodsCategory_data)

    def test_getGoodsCategory1(self):
        '''token正确'''
        getGoodsCategory_data={'token':self.token}
        r=requests.get(url=self.getGoodsCategory_url,headers=self.headers,params=getGoodsCategory_data)
        print(r.json())
        self.assertEqual(r.json()['execute_status'],'success')

    def test_getGoodsCategory2(self):
        '''token不正确'''
        token ='e'
        getGoodsCategory_data={'token':token}
        r=requests.get(url=self.getGoodsCategory_url,headers=self.headers,params=getGoodsCategory_data)
        print(r.json())
        self.assertEqual(r.json(),'Token error')



if __name__ == '__main__':
    GetGoodsCategory().__init__()