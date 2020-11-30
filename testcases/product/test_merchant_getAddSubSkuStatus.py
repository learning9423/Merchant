import random
import unittest

import requests

from common.read_excel import ReadExcel
from common.send_request import SendRequest

getAddProductSku_data=ReadExcel().readExcel(r'../data/getAddProductSku_api.xlsx','Sheet1')
s=requests.session()
class GetAddSubSkuStatus(unittest.TestCase):
    '''获取新增子sku状态'''
    @classmethod
    def setUpClass(cls):

        for i in range(len(getAddProductSku_data)):
            if '{upload_batch_id}' in getAddProductSku_data[i]['body']:
                getAddProductSku_data[i]['body']=getAddProductSku_data[i]['body'].replace('{upload_batch_id}',self.get_upload_batch_id())
            else:
                continue

    def get_upload_batch_id(self):
        '''获取新增子sku的批次id'''
        addProductSku_url = 'https://m-t1.vova.com.hk/api/v1/product/addProductSku'
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
        addProductSku_data = {
            "token": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo',
            "items": [
                {
                    "parent_sku": "5673422g3ff",
                    "goods_sku": "w1"+str(random.randint(0,10000)),
                    "storage": 100,
                    "market_price": 11,
                    "shop_price": 12,
                    "shipping_fee": 4,
                    "style_array": {
                        "size": "125kg",
                        "color": "red",
                        "style_quantity": "600"+str(random.randint(0,10000))
                    },
                    "sku_image": "http://img.gaoxiaogif.com/d/file/201908/8ae30f4f63595bd2db1bf0a21333979a.gif"
                }
            ]
        }
        r=requests.post(url=addProductSku_url,headers=headers,json=addProductSku_data)
        return r.json()['data']['upload_batch_id']

    def test_getAddProductSku1(self):
        '''token与批次id都正确'''
        r=SendRequest.sendRequest(s,getAddProductSku_data[0])
        expect_result1=getAddProductSku_data[0]['expect_result'].split(":")[1]
        expect_result2=getAddProductSku_data[0]['expect_result'].split(":")[2]
        if r.json()['execute_status']=='partial_success':
            self.assertEqual(r.json()['execute_status'],eval(expect_result1),msg=r.json())
        else:
            self.assertEqual(r.json()['execute_status'],eval(expect_result2),msg=r.json())

    def test_getAddProductSku2(self):
        '''token不正确，批次id正确'''
        r=SendRequest.sendRequest(s,getAddProductSku_data[1])
        expect_result=getAddProductSku_data[1]['expect_result'].split(":")[1]
        self.assertEqual(r.json(),eval(expect_result),msg=r.json())

    def test_getAddProductSku3(self):
        '''token正确，批次id正确'''
        r=SendRequest.sendRequest(s,getAddProductSku_data[2])
        expect_result=getAddProductSku_data[2]['expect_result'].split(":")[1]
        msg=getAddProductSku_data[2]['msg'].split(":")[1]

        self.assertEqual(r.json()['execute_status'],eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['message'],eval(msg),msg=r.json())
if __name__ == '__main__':
    GetAddSubSkuStatus().test_getAddProductSku3()