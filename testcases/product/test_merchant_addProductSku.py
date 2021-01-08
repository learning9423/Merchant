import random
import unittest
from pip._vendor import requests
from common.read_excel import ReadExcel
from common.send_request import SendRequest
from common.sql_data import SqlData

addProductSku_data=ReadExcel().readExcel(r'../data/addProductSku_api.xlsx', 'Sheet1')
s=requests.session()
class AddProductSku(unittest.TestCase):
    '''新增子sku'''
    @classmethod
    def setUpClass(cls):
        for i in range(len(addProductSku_data)):
            if addProductSku_data[i]['sql']!='' and '{parent_sku}' in addProductSku_data[i]['body']:
                a=SqlData.themis_data(addProductSku_data[i]['sql'])
                addProductSku_data[i]['body']=addProductSku_data[i]['body'].replace('{parent_sku}',''.join('%s' %id for id in a[i]))
            if '{goods_sku}' in addProductSku_data[i]['body']:
                addProductSku_data[i]['body']=addProductSku_data[i]['body'].replace('{goods_sku}','r'+str(random.randint(1,10000)))
            if '{style_quantity}' in addProductSku_data[i]['body']:
                addProductSku_data[i]['body']=addProductSku_data[i]['body'].replace('{style_quantity}',str(random.randint(1,10000)))
            else:
                continue

    def test_addProductSku1(self):
        '''token及参数都正确'''
        r=SendRequest.sendRequest(s,addProductSku_data[0])
        expect_result=addProductSku_data[0]['expect_result'].split(":",1)[1]
        msg=addProductSku_data[0]['msg'].split(":",1)[1]
        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['message'], eval(msg),msg=r.json())

    def test_addProductSku2(self):
        '''新增sku参数重复'''
        r=SendRequest.sendRequest(s,addProductSku_data[0])
        expect_result=addProductSku_data[1]['expect_result'].split(":",1)[1]
        msg=addProductSku_data[1]['msg'].split(":",1)[1]
        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['code'], eval(msg),msg=r.json())

    def test_addProductSku3(self):
        '''token正确，参数为空'''
        r=SendRequest.sendRequest(s,addProductSku_data[2])
        expect_result=addProductSku_data[2]['expect_result'].split(":",1)[1]
        msg=addProductSku_data[2]['msg'].split(":",1)[1]+':'+addProductSku_data[2]['msg'].split(":")[2]
        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['errors_list'][0]['message'], eval(msg),msg=r.json())


    def test_addProductSku4(self):
        '''token不正确，其余参数都正确'''
        r=SendRequest.sendRequest(s,addProductSku_data[3])
        expect_result=addProductSku_data[3]['expect_result'].split(":",1)[1]
        self.assertEqual(r.json(), eval(expect_result),msg=r.json())

if __name__ == '__main__':
    AddProductSku().test_addProductSku3()



