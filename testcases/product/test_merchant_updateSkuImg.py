import unittest
import pymysql
from pip._vendor import requests

from common.read_excel import ReadExcel
from common.send_request import SendRequest
from common.sql_data import SqlData


class UpdateSkuImg(unittest.TestCase):
    '''更新商品sku图片'''
    def __init__(self):
        self.updateSkuImg_data=ReadExcel().readExcel(r'../../data/updateSkuImg_api.xlsx','Sheet1')
        for i in range(len(self.updateSkuImg_data)):
            a = SqlData.themis_data(self.updateSkuImg_data[i]['sql'])
            if self.updateSkuImg_data[i]['sql']!='' and '{product_id}' in self.updateSkuImg_data[i]['body']:
                self.updateSkuImg_data[i]['body']=self.updateSkuImg_data[i]['body'].replace('{product_id}',str(a[i][0]))
            elif self.updateSkuImg_data[i]['sql']!='' and '{goods_sku}' in self.updateSkuImg_data[i]['body']:
                self.updateSkuImg_data[i]['body']=self.updateSkuImg_data[i]['body'].replace('{goods_sku}',''.join('%s' %id for id in a[i][1]))
            elif self.updateSkuImg_data[i]['sql']!='' and '{img_id}' in self.updateSkuImg_data[i]['body']:
                self.updateSkuImg_data[i]['body']=self.updateSkuImg_data[i]['body'].replace('{img_id}',''.join('%s' %id for id in a[i][2]))
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
        '''克隆商品不能更新图片'''
        cur=self.find_productData()
        cur.execute(self.sql2)
        self.con.commit()
        result=cur.fetchall()
        updateSkuImg_data={'token':self.token,'product_id':result[0][0],'sku_img_info':[{'goods_sku':result[0][1],'img_id':str(result[0][2])}]}

        r=requests.post(url=self.updateSkuImg_url,headers=self.headers,json=updateSkuImg_data)
        print(r.json())
        print('更新的商品信息为：%s'%updateSkuImg_data['product_id'],updateSkuImg_data['sku_img_info'])
        self.assertEqual(r.json()['execute_status'], 'failed')
        self.assertEqual(r.json()['data']['code'] ,41019)

    def test_updateSkuImg3(self):
        '''token正确，其余参数为空或无效'''
        cur=self.find_productData()
        cur.execute(self.sql1)
        self.con.commit()
        result=cur.fetchall()

        for i in range(3):
             if i==0:
                updateSkuImg_data={'token':self.token,'product_id':'','sku_img_info':[{'goods_sku':result[0][1],'img_id':str(result[0][2])}]}
                r=requests.post(url=self.updateSkuImg_url,headers=self.headers,json=updateSkuImg_data)
                print(r.json())
                self.assertEqual(r.json()['execute_status'], 'failed')
                self.assertEqual(r.json()['data']['code'] ,40001)
             elif i==1:
                updateSkuImg_data={'token':self.token,'product_id':result[0][0],'sku_img_info':[{'goods_sku':'a','img_id':str(result[0][2])}]}
                r=requests.post(url=self.updateSkuImg_url,headers=self.headers,json=updateSkuImg_data)
                print(r.json())
                self.assertEqual(r.json()['execute_status'], 'failed')
                self.assertEqual(r.json()['data']['errors_list'][0]['code'] ,41020)
             elif i==2:
                updateSkuImg_data={'token':self.token,'product_id':result[0][0],'sku_img_info':[{'goods_sku':result[0][1],'img_id':'a1'}]}
                r=requests.post(url=self.updateSkuImg_url,headers=self.headers,json=updateSkuImg_data)
                print(r.json())
                self.assertEqual(r.json()['execute_status'], 'failed')
                self.assertEqual(r.json()['data']['errors_list'][0]['code'] ,41021)

    def test_updateSkuImg4(self):
        '''token错误，其余参数正确'''
        cur=self.find_productData()
        cur.execute(self.sql1)
        self.con.commit()
        result=cur.fetchall()
        token='e'
        updateSkuImg_data={'token':token,'product_id':result[0][0],'sku_img_info':[{'goods_sku':result[0][1],'img_id':str(result[0][2])}]}

        r=requests.post(url=self.updateSkuImg_url,headers=self.headers,json=updateSkuImg_data)
        print(r.json())
        self.assertEqual(r.json(), 'Token error')

if __name__ == '__main__':
    UpdateSkuImg().test_updateSkuImg1()
