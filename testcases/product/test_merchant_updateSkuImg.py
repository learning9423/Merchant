import unittest
from pip._vendor import requests

from common.read_excel import ReadExcel
from common.send_request import SendRequest
from common.sql_data import SqlData

updateSkuImg_data=ReadExcel().readExcel(r'../data/updateSkuImg_api.xlsx','Sheet1')
s = requests.session()
class UpdateSkuImg(unittest.TestCase):
    '''更新商品sku图片'''
    @classmethod
    def setUpClass(cls):
        for i in range(len(updateSkuImg_data)):
            if updateSkuImg_data[i]['sql']!='':
                a = SqlData.themis_data(updateSkuImg_data[i]['sql'])
                if '{product_id}' in updateSkuImg_data[i]['body']:
                    updateSkuImg_data[i]['body']=updateSkuImg_data[i]['body'].replace('{product_id}',str(a[i][0]))
                if '{goods_sku}' in updateSkuImg_data[i]['body']:
                    updateSkuImg_data[i]['body']=updateSkuImg_data[i]['body'].replace('{goods_sku}',str(a[i][1]))
                if '{img_id}' in updateSkuImg_data[i]['body']:
                    updateSkuImg_data[i]['body']=updateSkuImg_data[i]['body'].replace('{img_id}',str(a[i][2]))
            else:
                continue

    def test_updateSkuImg1(self):
        '''token和参数都正确'''
        r = SendRequest.sendRequest(s, updateSkuImg_data[0])
        expect_result = updateSkuImg_data[0]['expect_result'].split(":",1)[1]
        msg = updateSkuImg_data[0]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['code'] ,eval(msg),msg=r.json())

    def test_updateSkuImg2(self):
        '''token错误，其余参数正确'''
        r = SendRequest.sendRequest(s, updateSkuImg_data[1])
        expect_result = updateSkuImg_data[1]['expect_result'].split(":",1)[1]

        self.assertEqual(r.json(), eval(expect_result),msg=r.json())

    def test_updateSkuImg3(self):
        '''token正确，product_id错误'''
        r = SendRequest.sendRequest(s, updateSkuImg_data[2])
        expect_result = updateSkuImg_data[2]['expect_result'].split(":",1)[1]
        msg = updateSkuImg_data[2]['msg'].split(":",1)[1]
        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['code'] ,eval(msg),msg=r.json())

    def test_updateSkuImg4(self):
        '''token正确，goods_sku错误'''
        r = SendRequest.sendRequest(s, updateSkuImg_data[3])
        expect_result = updateSkuImg_data[3]['expect_result'].split(":",1)[1]
        msg = updateSkuImg_data[3]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['errors_list'][0]['code'] ,eval(msg),msg=r.json())

    def test_updateSkuImg5(self):
        '''token正确，img_id错误'''
        r = SendRequest.sendRequest(s, updateSkuImg_data[4])
        expect_result = updateSkuImg_data[4]['expect_result'].split(":",1)[1]
        msg = updateSkuImg_data[4]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['errors_list'][0]['code'] ,eval(msg),msg=r.json())

if __name__ == '__main__':
    UpdateSkuImg().test_updateSkuImg5()
