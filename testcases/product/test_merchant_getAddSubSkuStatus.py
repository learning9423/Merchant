import random
import unittest

import requests


class GetAddSubSkuStatus(unittest.TestCase):
    '''获取新增子sku状态'''
    getAddProductSku_url='https://m-t1.vova.com.hk/api/v1/product/getAddSubSkuStatus'
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
    def setUp(self):
        '''获取新增子sku的批次id'''
        addProductSku_url = 'https://m-t1.vova.com.hk/api/v1/product/addProductSku'
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
        addProductSku_data = {
            "token": self.token,
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
        data={'token':self.token,'conditions':{'upload_batch_id':self.setUp()}}
        r=requests.post(url=self.getAddProductSku_url,headers=self.headers,json=data)
        print(r.json())
        if r.json()['execute_status']=='partial_success':
            self.assertEqual(r.json()['execute_status'],'partial_success')
        else:
            self.assertEqual(r.json()['execute_status'],'success')

    def test_getAddProductSku2(self):
        '''token不正确，批次id正确'''
        data={'token':'e','conditions':{'upload_batch_id':self.setUp()}}
        r=requests.post(url=self.getAddProductSku_url,headers=self.headers,json=data)
        print(r.json())
        self.assertEqual(r.json(),'Token error')

    def test_getAddProductSku3(self):
        '''token正确，批次id正确'''
        data={'token':self.token,'conditions':{'upload_batch_id':'3'}}
        r=requests.post(url=self.getAddProductSku_url,headers=self.headers,json=data)
        print(r.json())
        self.assertEqual(r.json()['execute_status'],'failed')
        self.assertEqual(r.json()['data']['message'],'不是新增子sku的批次')

if __name__ == '__main__':
    GetAddSubSkuStatus().test_getAddProductSku3()