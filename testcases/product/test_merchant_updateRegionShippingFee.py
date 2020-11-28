import unittest
from pip._vendor import requests

from common.read_excel import ReadExcel
from common.send_request import SendRequest
from common.sql_data import SqlData


class UpdateRegionShippingFee(unittest.TestCase):
    '''更新国家运费'''

    def __init__(self,methodName='runTest'):
        # 数据初始化
        super(UpdateRegionShippingFee,self).__init__(methodName)
        self.updateRegionShippingFee_data = ReadExcel().readExcel(r'../data/updateRegionShippingFee_api.xlsx','Sheet1')
        for i in range(len(self.updateRegionShippingFee_data)):
            if self.updateRegionShippingFee_data[i]['sql'] != '' and '{parent_sku}' in self.updateRegionShippingFee_data[i]['body']:
                a = SqlData.themis_data(self.updateRegionShippingFee_data[i]['sql'])
                self.updateRegionShippingFee_data[i]['body'] = self.updateRegionShippingFee_data[i]['body'].replace('{parent_sku}',str(a[i]))
            else:
                continue
        self.s = requests.session()
        self._type_equality_funcs = {}


    def test_updateRegionShippingFee1(self):
        '''token与运费参数都正确'''
        r = SendRequest.sendRequest(self.s, self.updateRegionShippingFee_data[0])
        expect_result = self.updateRegionShippingFee_data[0]['expect_result'].split(":")[1]
        msg = self.updateRegionShippingFee_data[0]['msg'].split(":")[1]
        self.assertEqual(r.json()['execute_status'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['message'], eval(msg), msg=r.json())

    def test_updateRegionShippingFee2(self):
        '''token错误，运费参数正确'''
        r = SendRequest.sendRequest(self.s, self.updateRegionShippingFee_data[1])
        expect_result = self.updateRegionShippingFee_data[1]['expect_result'].split(":")[1]
        self.assertEqual(r.json(), eval(expect_result), msg=r.json())

    def test_updateRegionShippingFee3(self):
        '''token正确，运费参数不正确'''
        r = SendRequest.sendRequest(self.s, self.updateRegionShippingFee_data[2])
        expect_result = self.updateRegionShippingFee_data[2]['expect_result'].split(":")[1]
        msg = self.updateRegionShippingFee_data[2]['msg'].split(":")[1]
        self.assertEqual(r.json()['execute_status'], eval(expect_result), msg=r.json())
        self.assertEqual(r.json()['message'], eval(msg), msg=r.json())

if __name__ == '__main__':
    UpdateRegionShippingFee().test_updateRegionShippingFee3()
