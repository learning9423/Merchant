import unittest
from pip._vendor import requests
from common.read_excel import ReadExcel
from common.send_request import SendRequest
from common.sql_data import SqlData

updateGoodsByType_data=ReadExcel().readExcel(r'../data/updateGoodsByType_api.xlsx','Sheet1')
s=requests.session()
class UpdateGoodsByType(unittest.TestCase):
    '''修改商品名称、描述或分类'''

    @classmethod
    def setUpClass(cls):
        for i in range(len(updateGoodsByType_data)):
            if updateGoodsByType_data[i]['sql'] != '' and '{virtual_goods_id}' in updateGoodsByType_data[i]['body']:
                a=SqlData.themis_data(updateGoodsByType_data[i]['sql'])
                updateGoodsByType_data[i]['body']=updateGoodsByType_data[i]['body'].replace('{virtual_goods_id}',''.join('%s' %id for id in a[i]))

    def test_updateGoodsByType1(self):
        '''修改商品名称'''

        r=SendRequest.sendRequest(s,updateGoodsByType_data[0])
        expect_result = updateGoodsByType_data[0]['expect_result'].split(":",1)[1]
        msg = updateGoodsByType_data[0]['msg'].split(":",1)[1]
        print(r.json())
        print(updateGoodsByType_data)

        self.assertEqual(r.json()['execute_status'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['message'], eval(msg), msg=r.json())

    def test_updateGoodsByType2(self):
        '''修改商品描述'''
        r=SendRequest.sendRequest(s,updateGoodsByType_data[1])
        expect_result = updateGoodsByType_data[1]['expect_result'].split(":",1)[1]
        msg = updateGoodsByType_data[1]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['message'], eval(msg), msg=r.json())

    def test_updateGoodsByType3(self):
        '''修改商品分类'''
        r=SendRequest.sendRequest(s,updateGoodsByType_data[2])
        expect_result = updateGoodsByType_data[2]['expect_result'].split(":",1)[1]
        msg = updateGoodsByType_data[2]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['message'], eval(msg), msg=r.json())

    def test_updateGoodsByType4(self):
        '''克隆商品无法更改'''
        r=SendRequest.sendRequest(s,updateGoodsByType_data[3])
        expect_result = updateGoodsByType_data[3]['expect_result'].split(":",1)[1]
        msg = updateGoodsByType_data[3]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['message'], eval(msg), msg=r.json())

    def test_updateGoodsByType5(self):
        '''参数为空'''
        r=SendRequest.sendRequest(s,updateGoodsByType_data[4])
        expect_result = updateGoodsByType_data[4]['expect_result'].split(":",1)[1]
        msg = updateGoodsByType_data[4]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['message'], eval(msg), msg=r.json())

    def test_updateGoodsByType6(self):
        '''参数错误'''
        r=SendRequest.sendRequest(s,updateGoodsByType_data[5])
        expect_result = updateGoodsByType_data[5]['expect_result'].split(":",1)[1]
        msg = updateGoodsByType_data[5]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['message'], eval(msg), msg=r.json())

    def test_updateGoodsByType7(self):
        '''token错误'''
        r=SendRequest.sendRequest(s,updateGoodsByType_data[6])
        expect_result = updateGoodsByType_data[6]['expect_result'].split(":",1)[1]
        msg = updateGoodsByType_data[6]['msg'].split(":",1)[1]

        self.assertEqual(r.json()['execute_status'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['message'], eval(msg), msg=r.json())


if __name__ == '__main__':
    UpdateGoodsByType().test_updateGoodsByType1()