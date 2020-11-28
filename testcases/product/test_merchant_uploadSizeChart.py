import unittest

from pip._vendor import requests
from common.read_excel import ReadExcel
from common.send_request import SendRequest
from common.sql_data import SqlData


class UploadSizeChart(unittest.TestCase):
    '''上传商品尺寸信息'''
    def __init__(self,methodName='runTest'):
        # 数据初始化
        super(UploadSizeChart,self).__init__(methodName)
        self.uploadSizeChart_data=ReadExcel().readExcel(r'../../data/uploadSizeChart_api.xlsx','Sheet1')
        for i in range(len(self.uploadSizeChart_data)):
            if self.uploadSizeChart_data[i]['sql']!='':
                a=SqlData.themis_data(self.uploadSizeChart_data[i]['sql'])
                if '{product_id}' in self.uploadSizeChart_data[i]['body']:
                    self.uploadSizeChart_data[i]['body']=self.uploadSizeChart_data[i]['body'].replace('{product_id}',''.join('%s' %id for id in a[i]))
                    if '{product_id}' in self.uploadSizeChart_data[i]['expect_result']:
                        self.uploadSizeChart_data[i]['expect_result']=self.uploadSizeChart_data[i]['expect_result'].replace('{product_id}',''.join('%s' %id for i in a[i]))
            else:
                continue
        self.s = requests.session()
        self._type_equality_funcs = {}

    def test_uploadSizeChart1(self):
        '''token与尺寸参数都正确'''
        r = SendRequest.sendRequest(self.s, self.uploadSizeChart_data[0])
        expect_result = self.uploadSizeChart_data[0]['expect_result'].split(":")[1]
        msg = self.uploadSizeChart_data[0]['msg'].split(":")[1]
        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['message'],eval(msg),msg=r.json())

    def test_uploadSizeChart2(self):
        '''token不正确，尺寸参数正确'''
        r = SendRequest.sendRequest(self.s, self.uploadSizeChart_data[1])
        expect_result = self.uploadSizeChart_data[1]['expect_result'].split(":")[1]
        self.assertEqual(r.json(), eval(expect_result),msg=r.json())

    def test_uploadSizeChart3(self):
        '''token正确，尺寸参数错误'''
        r = SendRequest.sendRequest(self.s, self.uploadSizeChart_data[2])
        expect_result = self.uploadSizeChart_data[2]['expect_result'].split(":")[1]
        msg = self.uploadSizeChart_data[2]['msg'].split(":")[1]
        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['message'],eval(msg),msg=r.json())

    def test_uploadSizeChart4(self):
        '''token正确，product_id错误'''
        r = SendRequest.sendRequest(self.s, self.uploadSizeChart_data[3])
        expect_result = self.uploadSizeChart_data[3]['expect_result'].split(":")[1]
        msg = self.uploadSizeChart_data[3]['msg'].split(":")[1]
        self.assertEqual(r.json()['execute_status'], eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['message'],eval(msg),msg=r.json())

if __name__ == '__main__':
    UploadSizeChart().test_uploadSizeChart4()