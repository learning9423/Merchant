import json
import unittest
from pip._vendor import requests
from common.read_excel import ReadExcel
from common.send_request import SendRequest
from common.sql_data import SqlData


class AbleSale():
    '''商品上架'''
    ableSale_data = ReadExcel().readExcel(r'../data/ableSale&enableSale_api.xlsx', 'Sheet1')
    s = requests.session()

    def test_ableSale1(self):
        '''token和商品id都正确'''

        print(type(self.ableSale_data[0]['sql']))
        b=SqlData.themis_data(self.ableSale_data[0]['sql'])
        print(print(type(eval(self.ableSale_data[0]['body'])['goods_list'])))

        # r=SendRequest.sendRequest(self.s,self.ableSale_data[0])
        # print(self.ableSale_data[0])
        # expect_result=eval(self.ableSale_data[0]['expect_result']).spilt(':')[1]
        # msg=eval(self.ableSale_data[0]['msg']).spilt(':')[1]
        #
        # self.assertEqual(r.json()['execute_status'],expect_result,msg=r.json())
        # self.assertEqual(r.json()['data']['code'],msg,msg=r.json())

    def test_ableSale2(self):
        '''商品id错误'''

        ableSale_data = {'token': self.token, 'goods_list': [124]}

        r = requests.post(url=self.ableSale_url, json=ableSale_data, headers=self.headers)
        print(r.json())
        self.assertEqual(r.json()['data']['errors_list'][0]['code'], 41001)

    def test_ableSale3(self):
        '''token错误'''
        cur = self.find_productId()
        cur.execute(self.sql)
        self.con.commit()
        result = cur.fetchall()
        token = 'e'
        ableSale_data = {'token': token, 'goods_list': result[0]}

        r = requests.post(url=self.ableSale_url, json=ableSale_data, headers=self.headers)
        print(r.json())
        self.assertEqual(r.text, '"Token error"')
        self.assertEqual(r.status_code, 401)


if __name__ == '__main__':
    AbleSale().test_ableSale1()
