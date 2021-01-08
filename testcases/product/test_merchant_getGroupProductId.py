import unittest

from pip._vendor import requests

from common.read_excel import ReadExcel
from common.send_request import SendRequest
from common.sql_data import SqlData

getGroupProductId_data=ReadExcel().readExcel(r'../data/getGroupProductId_api.xlsx','Sheet1')
s=requests.session()
class GetGroupProductId(unittest.TestCase):
    '''根据商品id获取同组gsn商品'''
    @classmethod
    def setUpClass(cls) :
        for i in range(len(getGroupProductId_data)):
            if getGroupProductId_data[i]['sql']!='' and '{virtual_goods_id}' in getGroupProductId_data[i]['body']:
                a=SqlData.themis_data(getGroupProductId_data[i]['sql'])
                getGroupProductId_data[i]['body']=getGroupProductId_data[i]['body'].replace('{virtual_goods_id}',''.join('%s' %id for id in a[i]))
                if '{virtual_goods_id}' in getGroupProductId_data[i]['msg']:
                    getGroupProductId_data[i]['msg']=getGroupProductId_data[i]['msg'].replace('{virtual_goods_id}',''.join('%s' %id for id in a[i]))
            else:
                continue

    def test_getGroupProductId1(self):
        '''商品id正确，token正确'''
        r=SendRequest.sendRequest(s,getGroupProductId_data[0])
        expect_result=getGroupProductId_data[0]['expect_result'].split(":",1)[1]
        msg=getGroupProductId_data[0]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'],eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data'][0]['goods_id'],eval(msg),msg=r.json())

    def test_getGroupProductId2(self):
        '''商品id正确，token错误'''
        r=SendRequest.sendRequest(s,getGroupProductId_data[1])
        expect_result=getGroupProductId_data[1]['expect_result'].split(":",1)[1]

        self.assertEqual(r.json(),eval(expect_result),msg=r.json())

    def test_getGroupProductId3(self):
        '''商品id为空，token正确'''
        r=SendRequest.sendRequest(s,getGroupProductId_data[2])
        expect_result=getGroupProductId_data[2]['expect_result'].split(":",1)[1]
        msg=getGroupProductId_data[2]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'],eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['message'],eval(msg),msg=r.json())

    def test_getGroupProductId4(self):
        '''商品id错误，token正确'''
        r=SendRequest.sendRequest(s,getGroupProductId_data[3])
        expect_result=getGroupProductId_data[3]['expect_result'].split(":",1)[1]
        msg=getGroupProductId_data[3]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'],eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['message'],eval(msg),msg=r.json())

if __name__ == '__main__':
    GetGroupProductId().test_getGroupProductId2()