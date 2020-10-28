import random
import unittest
from pip._vendor import requests

from common.read_excel import ReadExcel
from common.send_request import SendRequest


class AddProductSku(unittest.TestCase):
    '''新增子sku'''
    def __init__(self):
        self.addProductSku_data=ReadExcel().readExcel(r'../data/addProductSku_api.xlsx','Sheet1')
        for i in range(len(self.addProductSku_data)):
            if '{goods_sku}' not in self.addProductSku_data[i]['body']:
                self.addProductSku_data[i]['body']=self.addProductSku_data[i]['body'].replace('{goods_sku}','t'+str(random(10000)))
                self.addProductSku_data[i]['body']=self.addProductSku_data[i]['body'].replace('{style_quantity}',str(random(10000)))
            else:
                continue
        self.s = requests.session()
        self._type_equality_funcs={}

    def test_addProductSku1(self):
        '''token及参数都正确'''
        r=SendRequest.sendRequest(self.addProductSku_data,self.s)
        expect_result=self.ableSale_data[0]['expect_result'].split(":")[1]
        msg=self.ableSale_data[0]['msg'].split(":")[1]
        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['message'], msg=r.json())

    def test_addProductSku2(self):
        '''新增sku参数重复'''
        r=requests.post(url=self.addProductSku_url,headers=self.headers,json=self.test_addProductSku1())
        print(r.json())
        self.assertEqual(r.json()['execute_status'], 'failed')
        self.assertEqual(r.json()['data']['code'], 40015)

    def test_addProductSku3(self):
        '''token正确，参数为空'''
        self.addProductSku_data['items'][0]['parent_sku']=''
        r=requests.post(url=self.addProductSku_url,headers=self.headers,json=self.addProductSku_data)
        print(r.json())
        self.assertEqual(r.json()['execute_status'], 'failed')
        self.assertEqual(r.json()['data']['errors_list'][0]['message'], '错误: 必填属性 parent_sku 不得为空')


    def test_addProductSku4(self):
        '''token不正确，其余参数都正确'''
        self.addProductSku_data['token']='e'
        self.addProductSku_data['items'][0]['parent_sku']='5673422g3ff'
        r=requests.post(url=self.addProductSku_url,headers=self.headers,json=self.addProductSku_data)
        print(r.json())
        self.assertEqual(r.json(), 'Token error')
if __name__ == '__main__':
    AddProductSku().test_addProductSku1()

