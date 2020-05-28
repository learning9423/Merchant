import unittest
import pymysql
from pip._vendor import requests
from retrying import retry


class disableSale(unittest.TestCase):
    sql1 = "select vg.virtual_goods_id from virtual_goods vg inner join goods g on g.goods_id=vg.goods_id where g.is_on_sale='1' and g.merchant_id='26420' and sale_status='normal' and is_delete='0' ;"
    sql2 = "select vg.virtual_goods_id from fbv_sku_warehouse_storage fsws inner join goods_sku gs on gs.sku_id = fsws.sku_id inner join goods g on g.goods_id = gs.goods_id inner join virtual_goods vg on vg.goods_id=g.goods_id where fsws.fbv_warehouse_storage!=0 and g.is_on_sale='1' and g.merchant_id ='13' and g.sale_status='normal';"
    sale_url = 'https://m-t1.vova.com.hk/api/v1/product/disableSale'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}

    @retry(stop_max_attempt_number=5, wait_random_max=1000)
    def find_one(self):
        self.con = pymysql.Connect(host='123.206.135.211',
                                   port=3306,
                                   user='vvxxthemis',
                                   password='q3YBGG6JxE67xcYY1s0jIyBY4OmKqhg=',
                                   database='themis')
        self.cur = self.con.cursor()
        self.cur.execute(self.sql1)
        self.con.commit()
        return self.cur.fetchall()

    @retry(stop_max_attempt_number=5, wait_random_max=1000)
    def find_two(self):
        self.con = pymysql.Connect(host='123.206.135.211',
                                   port=3306,
                                   user='vvxxthemis',
                                   password='q3YBGG6JxE67xcYY1s0jIyBY4OmKqhg=',
                                   database='themis')
        self.cur = self.con.cursor()
        self.cur.execute(self.sql2)
        self.con.commit()
        return self.cur.fetchall()

    def test_disableSale1(self):
        '''无海外仓直接下架:token和商品id都正确'''
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODY0MTI0NDQsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiNTI0IiwidU5hbWUiOiJhcTk0MjMifQ.xOyVDsRovgHeIS1RSHlZ-fmPX9jG6p__Lpq42PcJShg'
        result1 = self.find_one()
        i = 0
        while i<len(result1):
            data = {'token': token, 'goods_list': result1[i]}
            r = requests.post(url=self.sale_url, json=data, headers=self.headers)
            if r.json()['execute_status'] == 'failed':
                i += 1
                continue
            else:
                print(r.json())
                print('下架的商品id:%s' % data['goods_list'])
                self.assertEqual(r.json()['execute_status'], 'success')
                break

    def test_disableSale2(self):
        '''无海外仓直接下架:商品id错误'''
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODY0MTI0NDQsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiNTI0IiwidU5hbWUiOiJhcTk0MjMifQ.xOyVDsRovgHeIS1RSHlZ-fmPX9jG6p__Lpq42PcJShg'
        data = {'token': token, 'goods_list': [124]}

        r = requests.post(url=self.sale_url, json=data, headers=self.headers)
        print(r.json())
        self.assertEqual(r.json()['data']['errors_list'][0]['code'],41001)

    def test_disableSale3(self):
        '''无海外仓库存直接下架:token错误'''
        token = 'e'
        result1 = self.find_one()
        data = {'token': token, 'goods_list': result1[0]}

        r = requests.post(url=self.sale_url, json=data, headers=self.headers)
        print(r.json())
        self.assertEqual(r.text, '"Token error"')
        self.assertEqual(r.status_code, 401)

    def test_disableSale4(self):
        '''有海外仓库存:直接下架'''
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Mzk2NjU4NDIsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoidGVzdDEifQ.4C7GbksLP3xbbM2Y-5_SYYBb1aUYL_mZ9igQMxZhkpU'
        result2 = self.find_two()
        i = 0
        while i<len(result2):
            data = {'token': token, 'goods_list':result2[i],'fbv_disable_way':'disable'}
            r = requests.post(url=self.sale_url, json=data, headers=self.headers)
            if r.json()['execute_status'] == 'failed':
                i += 1
                continue
            else:
                print(r.json())
                print('下架的商品id:%s' % data['goods_list'])
                self.assertEqual(r.json()['execute_status'], 'success')
                break
    def test_disableSale5(self):
        '''有海外仓库存:清零标准仓库存不下架'''
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Mzk2NjU4NDIsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoidGVzdDEifQ.4C7GbksLP3xbbM2Y-5_SYYBb1aUYL_mZ9igQMxZhkpU'
        result2 = self.find_two()
        i = 0
        while i<len(result2):
            data = {'token': token, 'goods_list': result2[i],'fbv_disable_way':'clear'}
            r = requests.post(url=self.sale_url, json=data, headers=self.headers)
            if r.json()['execute_status'] == 'failed':
                i += 1
                continue
            else:
                print(r.json())
                print('标准仓清零的商品id:%s' % data['goods_list'])
                self.assertEqual(r.json()['execute_status'], 'success')
                break

if __name__ == '__main__':
    disableSale().test_disableSale1()
