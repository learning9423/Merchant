import unittest
from pip._vendor import requests

from common.read_excel import ReadExcel
from common.send_request import SendRequest
from common.sql_data import SqlData


class UpdateSkuImg(unittest.TestCase):
    '''更新商品sku图片'''
    def __init__(self,methodName='runTest'):
        # 数据初始化
        super(UpdateSkuImg,self).__init__(methodName)
        self.updateSkuImg_data=ReadExcel().readExcel(r'../../data/updateSkuImg_api.xlsx','Sheet1')
        for i in range(len(self.updateSkuImg_data)):
            if self.updateSkuImg_data[i]['sql']!='':
                a = SqlData.themis_data(self.updateSkuImg_data[i]['sql'])
                if '{product_id}' in self.updateSkuImg_data[i]['body']:
                    self.updateSkuImg_data[i]['body']=self.updateSkuImg_data[i]['body'].replace('{product_id}',str(a[i][0]))
                if '{goods_sku}' in self.updateSkuImg_data[i]['body']:
                    self.updateSkuImg_data[i]['body']=self.updateSkuImg_data[i]['body'].replace('{goods_sku}',str(a[i][1]))
                if '{img_id}' in self.updateSkuImg_data[i]['body']:
                    self.updateSkuImg_data[i]['body']=self.updateSkuImg_data[i]['body'].replace('{img_id}',str(a[i][2]))
            else:
                continue
        self.s = requests.session()
        self._type_equality_funcs = {}

    def test_updateSkuImg1(self):
        '''token和参数都正确'''
        r = SendRequest.sendRequest(self.s, self.updateSkuImg_data[0])
        expect_result = self.updateSkuImg_data[0]['expect_result'].split(":")[1]
        msg = self.updateSkuImg_data[0]['msg'].split(":")[1]

        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['code'] ,eval(msg),msg=r.json())

    def test_updateSkuImg2(self):
        '''token错误，其余参数正确'''
        r = SendRequest.sendRequest(self.s, self.updateSkuImg_data[1])
        expect_result = self.updateSkuImg_data[1]['expect_result'].split(":")[1]

        self.assertEqual(r.json(), eval(expect_result),msg=r.json())

    def test_updateSkuImg3(self):
        '''token正确，product_id错误'''
        r = SendRequest.sendRequest(self.s, self.updateSkuImg_data[2])
        expect_result = self.updateSkuImg_data[2]['expect_result'].split(":")[1]
        msg = self.updateSkuImg_data[2]['msg'].split(":")[1]
        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['code'] ,eval(msg),msg=r.json())

    def test_updateSkuImg4(self):
        '''token正确，goods_sku错误'''
        r = SendRequest.sendRequest(self.s, self.updateSkuImg_data[3])
        expect_result = self.updateSkuImg_data[3]['expect_result'].split(":")[1]
        msg = self.updateSkuImg_data[3]['msg'].split(":")[1]

        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['errors_list'][0]['code'] ,eval(msg),msg=r.json())

    def test_updateSkuImg5(self):
        '''token正确，img_id错误'''
        r = SendRequest.sendRequest(self.s, self.updateSkuImg_data[4])
        expect_result = self.updateSkuImg_data[4]['expect_result'].split(":")[1]
        msg = self.updateSkuImg_data[4]['msg'].split(":")[1]

        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['errors_list'][0]['code'] ,eval(msg),msg=r.json())

if __name__ == '__main__':
    UpdateSkuImg().test_updateSkuImg5()
