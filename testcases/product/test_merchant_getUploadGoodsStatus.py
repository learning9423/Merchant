import random
import unittest

from pip._vendor import requests


class GetUploadGoodsStatus(unittest.TestCase):
    '''获取商品上传状态'''
    getUploadGoodsStatus_url="https://m-t1.vova.com.hk/api/v1/product/getUploadGoodsStatus"
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
    token ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'
    def setUp(self):
        '''上传商品获得商品批次id'''
        url = "https://m-t1.vova.com.hk/api/v1/product/uploadGoods"
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
        parent_sku='a'+str(random.randint(1,10000))
        data = {
            "token":self.token,
            "items": [{
                "cat_id": "5872",
                "parent_sku": parent_sku,
                "goods_sku": "eqwer",
                "goods_name": "avg",
                "storage": 12,
                "goods_description": "att G9",
                "tags": "",
                "goods_brand": "",
                "market_price": 22,
                "shop_price": 23,
                "shipping_fee": 2,
                "shipping_weight": 1,
                "shipping_time": "",
                "from_platform": "",
                "style_size": "400",
                "style_color": "green",
                "style_quantity": "200",
                "main_image": "http://img.gaoxiaogif.com/d/file/201908/8ae30f4f63595bd2db1bf0a21333979a.gif",
                "extra_image": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1582721500794&di=752f1e2ed42e10b0a6656f60a0270727&imgtype=0&src=http%3A%2F%2Fimages.liqucn.com%2Fimg%2Fh61%2Fh86%2Fimg_localize_fe2f4997a746a0befedbfac7b8370f3d.jpg"
            }],
            "ignore_warning": "1"
        }
        r_upload=requests.post(url=url,headers=headers,json=data)
        return r_upload

    def getUploadGoodsStatus1(self):
        '''token和批次id都正确'''
        r_upload=self.setUp()
        getUploadGoodsStatus_data={"token": self.token,"conditions": {"upload_batch_id": r_upload.json()['data']['upload_batch_id']}}

        r=requests.post(url=self.getUploadGoodsStatus_url,headers=self.headers,json=getUploadGoodsStatus_data)
        print(r.json())
        if r.json()['code']=='loading':
            self.assertEqual(r.json()['code'],'loading')
        else:
            self.assertEqual(r.json()['code'],'success')

    def getUploadGoodsStatus2(self):
        '''token不正确，批次id正确'''
        r_upload=self.setUp()
        token='e'
        getUploadGoodsStatus_data={"token": token,"conditions": {"upload_batch_id": r_upload.json()['data']['upload_batch_id']}}

        r=requests.post(url=self.getUploadGoodsStatus_url,headers=self.headers,json=getUploadGoodsStatus_data)
        print(r.json())
        self.assertEqual(r.json(),'Token error')

    def getUploadGoodsStatus3(self):
        '''token正确，批次id不正确'''
        getUploadGoodsStatus_data={"token": self.token,"conditions": {"upload_batch_id": 'e'}}

        r=requests.post(url=self.getUploadGoodsStatus_url,headers=self.headers,json=getUploadGoodsStatus_data)
        print(r.json())
        self.assertEqual(r.json()['code'],'error')
        self.assertEqual(r.json()['message'],'未查询到该批次的上传信息，请检查批次ID')

if __name__ == '__main__':
    GetUploadGoodsStatus().getUploadGoodsStatus3()