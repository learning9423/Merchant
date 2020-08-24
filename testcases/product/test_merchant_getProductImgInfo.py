import unittest

import pymysql
from pip._vendor import requests
from retrying import retry


class GetProductImgInfo(unittest.TestCase):
    sql = "select vg.virtual_goods_id from virtual_goods vg inner join goods g on g.goods_id=vg.goods_id where g.is_on_sale='0' and g.merchant_id='13' and g.is_delete='0';"
    getProductImgInfo_url = 'https://m-t1.vova.com.hk/api/v1/product/getProductImgInfo'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
    token ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'
    @retry(stop_max_attempt_number=5,wait_random_max=1000)
    def find_productData(self):
        self.con = pymysql.Connect(host='123.206.135.211',
                                   port=3306,
                                   user='vvxxthemis',
                                   password='q3YBGG6JxE67xcYY1s0jIyBY4OmKqhg=',
                                   database='themis')
        self.cur = self.con.cursor()
        self.cur.execute(self.sql)
        self.con.commit()
        return self.cur.fetchone()

    def test_getProductImgInfo1(self):
        '''token和商品id都正确'''
        result=self.find_productData()
        getProductImgInfo_data={'token':self.token,'product_id':result[0]}

        r=requests.get(url=self.getProductImgInfo_url,headers=self.headers,params=getProductImgInfo_data)
        print(r.json())
        self.assertEqual(r.json()['product_id'],str(getProductImgInfo_data['product_id']))

    def test_getProductImgInfo2(self):
        '''token不正确'''
        result=self.find_productData()
        token ='e'
        getProductImgInfo_data={'token':token,'product_id':result[0]}

        r=requests.get(url=self.getProductImgInfo_url,headers=self.headers,params=getProductImgInfo_data)
        print(r.json())
        self.assertEqual(r.json(),'Token error')

    def test_getProductImgInfo3(self):
        '''商品id为空或错误'''
        getProductImgInfo_data={'token':self.token,'product_id':""}

        r=requests.get(url=self.getProductImgInfo_url,headers=self.headers,params=getProductImgInfo_data)
        print(r.json())
        self.assertEqual(r.json()['product_id'],str(getProductImgInfo_data['product_id']))
        self.assertEqual(r.json()['message'],'查询为空')


if __name__ == '__main__':
    GetProductImgInfo().test_getProductImgInfo2()