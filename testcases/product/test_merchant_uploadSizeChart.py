import unittest

import pymysql
from pip._vendor import requests
from retrying import retry


class UploadSizeChart(unittest.TestCase):
    '''上传商品尺寸信息'''
    uploadSizeChart_url='https://m-t1.vova.com.hk/api/v1/product/uploadSizeChart'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
    sql1="select vg.virtual_goods_id from virtual_goods vg inner join goods g on g.goods_id=vg.goods_id where g.goods_sn like 'SN%' and g.merchant_id='13' and g.is_delete='0';"
    sql2="select vg.virtual_goods_id from virtual_goods vg inner join goods g on g.goods_id=vg.goods_id where g.goods_sn like 'GSN%' and g.merchant_id='13' and g.is_delete='0';"
    token ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'
    @retry(stop_max_attempt_number=5,wait_random_max=1000)
    def find_productData(self):
        self.con = pymysql.Connect(host='123.206.135.211',
                                   port=3306,
                                   user='vvxxthemis',
                                   password='q3YBGG6JxE67xcYY1s0jIyBY4OmKqhg=',
                                   database='themis')
        return self.con.cursor()

    def test_uploadSizeChart1(self):
        '''token与尺寸参数都正确'''
        cur=self.find_productData()
        cur.execute(self.sql1)
        result=cur.fetchone()
        uploadSizeChart_data={'token': self.token,'product_id': result[0],'size_data':[['Size', 'S','M', 'L'],['Shoulder', '35', '36', '37']],'size_remark':0 }

        r=requests.post(url=self.uploadSizeChart_url,headers=self.headers,json=uploadSizeChart_data)
        print(r.json())
        self.assertEqual(r.json()['execute_status'], 'success')
        self.assertEqual(r.json()['message'] ,'上传尺码数据成功')

    def test_uploadSizeChart2(self):
        '''克隆商品不能修改'''
        cur=self.find_productData()
        cur.execute(self.sql2)
        result=cur.fetchone()
        uploadSizeChart_data={'token': self.token,'product_id': result[0],'size_data':[['Size', 'S','M', 'L'],['Shoulder', '35', '36', '37']],'size_remark':0 }

        r=requests.post(url=self.uploadSizeChart_url,headers=self.headers,json=uploadSizeChart_data)
        print(r.json())
        self.assertEqual(r.json()['execute_status'], 'failed')
        self.assertEqual(r.json()['message'] ,'克隆商品，无法修改 ID :%s'%uploadSizeChart_data['product_id'])

    def test_uploadSizeChart3(self):
        '''token不正确，尺寸参数正确'''
        cur=self.find_productData()
        cur.execute(self.sql1)
        result=cur.fetchone()
        token='e'
        uploadSizeChart_data={'token': token,'product_id': result[0],'size_data':[['Size', 'S','M', 'L'],['Shoulder', '35', '36', '37']],'size_remark':0 }

        r=requests.post(url=self.uploadSizeChart_url,headers=self.headers,json=uploadSizeChart_data)
        print(r.json())
        self.assertEqual(r.json(), 'Token error')

    def test_uploadSizeChart4(self):
        '''token正确，尺寸参数不正确'''
        cur=self.find_productData()
        cur.execute(self.sql1)
        result=cur.fetchone()
        uploadSizeChart_data={'token': self.token,'product_id': result[0],'size_data':[['', 'S','M', 'L'],['Shoulder', '35', '36', '37']],'size_remark':0 }

        r=requests.post(url=self.uploadSizeChart_url,headers=self.headers,json=uploadSizeChart_data)
        print(r.json())
        self.assertEqual(r.json()['execute_status'], 'failed')

if __name__ == '__main__':
    UploadSizeChart().test_uploadSizeChart2()