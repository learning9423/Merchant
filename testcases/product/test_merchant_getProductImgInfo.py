import unittest
from pip._vendor import requests
from common.read_excel import ReadExcel
from common.send_request import SendRequest
from common.sql_data import SqlData

getProductImgInfo_data=ReadExcel().readExcel(r'../data/getProductImgInfo_api.xlsx', 'Sheet1')
s = requests.session()
class GetProductImgInfo(unittest.TestCase):
    '''获取商品图片信息'''
    @classmethod
    def setUpClass(cls):
        for i in range(len(getProductImgInfo_data)):
            if getProductImgInfo_data[i]['sql']!='' and '{virtual_goods_id}' in getProductImgInfo_data[i]['params']:
                a=SqlData.themis_data(getProductImgInfo_data[i]['sql'])
                getProductImgInfo_data[i]['params']=getProductImgInfo_data[i]['params'].replace('{virtual_goods_id}',''.join('%s' %id for id in a[i]))
                if '{virtual_goods_id}' in getProductImgInfo_data[i]['expect_result']:
                    getProductImgInfo_data[i]['expect_result'] = getProductImgInfo_data[i]['expect_result'].replace('{virtual_goods_id}', ''.join('%s' %id for id in a[i]))
            else:
                continue

    def test_getProductImgInfo1(self):
        '''token和商品id都正确'''
        r=SendRequest.sendRequest(s,getProductImgInfo_data[0])
        expect_result = getProductImgInfo_data[0]['expect_result'].split(":",1)[1]

        msg = getProductImgInfo_data[0]['msg'].split(":",1)[1]
        self.assertEqual(r.json()['product_id'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['message'], eval(msg), msg=r.json())


    def test_getProductImgInfo2(self):
        '''token不正确'''
        r=SendRequest.sendRequest(s,getProductImgInfo_data[1])
        expect_result=getProductImgInfo_data[1]['expect_result'].split(":",1)[1]
        self.assertEqual(r.json(), eval(expect_result), msg=r.json())

    def test_getProductImgInfo3(self):
        '''商品id为空或错误'''
        r = SendRequest.sendRequest(s, getProductImgInfo_data[2])
        expect_result = getProductImgInfo_data[2]['expect_result'].split(":",1)[1]
        msg = getProductImgInfo_data[2]['msg'].split(":",1)[1]
        self.assertEqual(r.json()['product_id'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['message'], eval(msg), msg=r.json())

if __name__ == '__main__':
    GetProductImgInfo().test_getProductImgInfo3()
