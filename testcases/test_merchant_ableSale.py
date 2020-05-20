import unittest
import pymysql
from pip._vendor import requests
from retrying import retry


class AbleSale(unittest.TestCase):
    sql = "select vg.virtual_goods_id from virtual_goods vg inner join goods g on g.goods_id=vg.goods_id where g.is_on_sale='0' and g.merchant_id='13' and g.is_delete='0' and g.sale_status='normal';"
    sale_url = 'https://m-t1.vova.com.hk/api/v1/product/enableSale'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}

    @retry(stop_max_attempt_number=5)
    def __init__(self):
        self.con = pymysql.Connect(host='123.206.135.211',
                                   port=3306,
                                   user='vvxxthemis',
                                   password='q3YBGG6JxE67xcYY1s0jIyBY4OmKqhg=',
                                   database='themis')
        # charset='utf-8'
        self._type_equality_funcs = {}

    def find_one(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.sql)
        self.con.commit()
        result=self.cur.fetchone()
        return result
    def test_ableSale1(self):
        '''token和商品id都正确'''
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Mzk2NjU4NDIsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoidGVzdDEifQ.4C7GbksLP3xbbM2Y-5_SYYBb1aUYL_mZ9igQMxZhkpU'
        data = {'token': token, 'goods_list': self.find_one()}

        r = requests.post(url=self.sale_url, json=data, headers=self.headers)
        print(data.get('goods_list'))
        print(r.json())

    def test_ableSale2(self):
        '''商品id错误'''
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Mzk2NjU4NDIsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoidGVzdDEifQ.4C7GbksLP3xbbM2Y-5_SYYBb1aUYL_mZ9igQMxZhkpU'
        data = {'token': token, 'goods_list': [124]}

        r = requests.post(url=self.sale_url, json=data, headers=self.headers)
        print(r.json())


    def test_ableSale3(self):
        '''token错误'''
        token = 'e'
        data = {'token': token, 'goods_list': self.find_one()}

        r = requests.post(url=self.sale_url, json=data, headers=self.headers)
        print(r.status_code)
        self.assertEqual(r.text, '"Token error"')
        self.assertEqual(r.status_code, 401)
        print(r.json())
