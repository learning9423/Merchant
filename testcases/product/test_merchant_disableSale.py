import unittest
import pymysql
from pip._vendor import requests
from retrying import retry

from common.read_excel import ReadExcel
from common.send_request import SendRequest


class DisableSale(unittest.TestCase):
    '''商品下架'''
    def __init__(self):
        # 数据初始化
        self.disableSale_data = ReadExcel().readExcel(r'../data/ableSale&enableSale_api.xlsx', 'Sheet2')
        self.s = requests.session()
        self._type_equality_funcs={}

    def test_disableSale1(self):
        '''无海外仓直接下架:token和商品id都正确'''
        r=SendRequest.sendRequest(self.s,self.disableSale_data[0])
        expect_result=self.disableSale_data[0]['expect_result'].split(":")[1]
        msg=self.disableSale_data[0]['msg'].split(":")[1]

        self.assertEqual(r.json()['execute_status'],eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['code'],eval(msg),msg=r.json())

    def test_disableSale2(self):
        '''无海外仓直接下架:商品id错误'''
        disableSale_data = {'token': self.token, 'goods_list': [124]}

        r = requests.post(url=self.disableSale_url, json=disableSale_data, headers=self.headers)
        print(r.json())
        self.assertEqual(r.json()['data']['errors_list'][0]['code'],41001)

    def test_disableSale3(self):
        '''无海外仓库存直接下架:token错误'''
        cur=self.find_productData()
        cur.execute(self.sql1)
        self.con.commit()
        result=cur.fetchall()
        token = 'e'
        disableSale_data = {'token': token, 'goods_list': result[0]}
        r = requests.post(url=self.disableSale_url, json=disableSale_data, headers=self.headers)
        print(r.json())
        self.assertEqual(r.text, '"Token error"')

    def test_disableSale4(self):
        '''有海外仓库存:直接下架'''
        r=SendRequest.sendRequest(self.s,self.disableSale_data[0])
        expect_result=self.disableSale_data[0]['expect_result'].split(":")[1]
        msg=self.disableSale_data[0]['msg'].split(":")[1]

        self.assertEqual(r.json()['execute_status'],eval(expect_result),msg=r.json())
        self.assertEqual(r.json()['data']['code'],eval(msg),msg=r.json())

    def test_disableSale5(self):
        '''有海外仓库存:清零标准仓库存不下架'''
        cur=self.find_productData()
        cur.execute(self.sql2)
        self.con.commit()
        result=cur.fetchall()

        i = 0
        while i<len(result):
            disableSale_data = {'token': self.token, 'goods_list': result[i],'fbv_disable_way':'clear'}
            r = requests.post(url=self.disableSale_url, json=disableSale_data, headers=self.headers)
            if r.json()['execute_status'] == 'failed':
                i += 1
                continue
            else:
                print(r.json())
                print('标准仓清零的商品id:%s' % disableSale_data['goods_list'])
                self.assertEqual(r.json()['execute_status'], 'success')
                break

if __name__ == '__main__':
    DisableSale().test_disableSale1()
