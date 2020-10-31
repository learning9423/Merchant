import random
import unittest
from pip._vendor import requests
from common.read_excel import ReadExcel
from common.send_request import SendRequest
from common.sql_data import SqlData


class AddProductSku(unittest.TestCase):
    '''新增子sku'''
    def __init__(self, requsts=None):
        self.addProductSku_data=ReadExcel().readExcel(r'../../data/addProductSku_api.xlsx', 'Sheet1')
        for i in range(len(self.addProductSku_data)):
            if self.addProductSku_data[i]['sql']!='' and '{parent_sku}' in self.addProductSku_data[i]['body']:
                a=SqlData.themis_data(self.addProductSku_data[i]['sql'])
                self.addProductSku_data[i]['body']=self.addProductSku_data[i]['body'].replace('{parent_sku}',''.join('%s' %id for id in a[i]))
            elif '{goods_sku}' in self.addProductSku_data[i]['body']:
                self.addProductSku_data[i]['body']=self.addProductSku_data[i]['body'].replace('{goods_sku}','r'+str(random.randint(1,10000)))
            elif '{style_quantity}' in self.addProductSku_data[i]['body']:
                self.addProductSku_data[i]['body']=self.addProductSku_data[i]['body'].replace('{style_quantity}',random.randint(1,10000))
            else:
                continue
        self.s=requests.session()
        self._type_equality_funcs={}

    def test_addProductSku1(self):
        '''token及参数都正确'''
        r=SendRequest.sendRequest(self.s,self.addProductSku_data[0])
        expect_result=self.addProductSku_data[0]['expect_result'].split(":")[1]
        msg=self.addProductSku_data[0]['msg'].split(":")[1]
        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['message'], eval(msg),msg=r.json())
        return self.addProductSku_data[0]
    def test_addProductSku2(self):
        '''新增sku参数重复'''
        r=SendRequest.sendRequest(self.s,self.test_addProductSku1())
        expect_result=self.addProductSku_data[1]['expect_result'].split(":")[1]
        msg=self.addProductSku_data[1]['msg'].split(":")[1]
        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['code'], eval(msg),msg=r.json())

    def test_addProductSku3(self):
        '''token正确，参数为空'''
        r=SendRequest.sendRequest(self.s,self.addProductSku_data[2])
        expect_result=self.addProductSku_data[2]['expect_result'].split(":")[1]
        msg=self.addProductSku_data[2]['msg'].split(":")[1]+':'+self.addProductSku_data[2]['msg'].split(":")[2]
        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['errors_list'][0]['message'], eval(msg),msg=r.json())


    def test_addProductSku4(self):
        '''token不正确，其余参数都正确'''
        r=SendRequest.sendRequest(self.s,self.addProductSku_data[3])
        expect_result=self.addProductSku_data[3]['expect_result'].split(":")[1]
        self.assertEqual(r.json(), eval(expect_result),msg=r.json())

if __name__ == '__main__':
    AddProductSku().test_addProductSku4()



