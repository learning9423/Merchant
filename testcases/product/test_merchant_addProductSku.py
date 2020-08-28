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
        self.assertEqual(r.json()['execute_status'], 'success')

if __name__ == '__main__':
    AddProductSku().test_addProductSku1()