import random
import unittest
from pip._vendor import requests
from common.read_excel import ReadExcel
from common.send_request import SendRequest

getUploadGoodsStatus_data=ReadExcel().readExcel(r'../data/getUploadGoodsStatus_api.xlsx','Sheet1')
s = requests.session()
class GetUploadGoodsStatus(unittest.TestCase):
    '''获取商品上传状态'''
    @classmethod
    def setUpClass(cls, self=None):
        url = "https://m-t1.vova.com.hk/api/v1/product/uploadGoods"
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
        parent_sku='a'+str(random.randint(1,10000))
        data = {
            "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo",
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
        for i in range(len(getUploadGoodsStatus_data)):
            if '{upload_batch_id}' in getUploadGoodsStatus_data[i]['body']:
                 getUploadGoodsStatus_data[i]['body']= getUploadGoodsStatus_data[i]['body'].replace('{upload_batch_id}', r_upload.json()['data']['upload_batch_id'])
            else:
                continue


    def test_getUploadGoodsStatus1(self):
        '''token和批次id都正确'''
        r = SendRequest.sendRequest(s, getUploadGoodsStatus_data[0])
        expect_result1 = getUploadGoodsStatus_data[0]['expect_result'].split(":")[1]
        expect_result2 = getUploadGoodsStatus_data[0]['expect_result'].split(":")[2]
        if r.json()['code']=='loading':
            self.assertEqual(r.json()['code'],eval(expect_result1),msg=r.json())
        else:
            self.assertEqual(r.json()['code'],eval(expect_result2),msg=r.json())

    def test_getUploadGoodsStatus2(self):
        '''token错误，批次id正确'''
        r = SendRequest.sendRequest(s, getUploadGoodsStatus_data[1])
        expect_result = getUploadGoodsStatus_data[1]['expect_result'].split(":")[1]
        self.assertEqual(r.json(),eval(expect_result))

    def test_getUploadGoodsStatus3(self):
        '''token正确，批次id错误'''
        r = SendRequest.sendRequest(s, getUploadGoodsStatus_data[2])
        expect_result = getUploadGoodsStatus_data[2]['expect_result'].split(":")[1]
        msg=getUploadGoodsStatus_data[2]['msg'].split(":")[1]
        self.assertEqual(r.json()['code'],eval(expect_result))
        self.assertEqual(r.json()['message'],eval(msg))

if __name__ == '__main__':
    GetUploadGoodsStatus().test_getUploadGoodsStatus3()