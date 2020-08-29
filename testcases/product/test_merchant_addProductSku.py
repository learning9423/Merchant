import random
import unittest
from pip._vendor import requests



class AddProductSku(unittest.TestCase):
    '''新增子sku'''
    sql = "select vg.virtual_goods_id from virtual_goods vg inner join goods g on g.goods_id=vg.goods_id where g.is_on_sale='0' and g.merchant_id='13' and g.is_delete='0';"
    addProductSku_url = 'https://m-t1.vova.com.hk/api/v1/product/addProductSku'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'
    addProductSku_data = {
            "token": token,
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

    def test_addProductSku1(self):
        '''token及参数都正确'''
        r=requests.post(url=self.addProductSku_url,headers=self.headers,json=self.addProductSku_data)
        print(r.json())
        return self.addProductSku_data
        self.assertEqual(r.json()['execute_status'], 'success')
        self.assertEqual(r.json()['data']['message'], '执行成功')

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
    AddProductSku().test_addProductSku3()

