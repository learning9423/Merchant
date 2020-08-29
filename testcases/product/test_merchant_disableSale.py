import unittest
import pymysql
from pip._vendor import requests
from retrying import retry


class DisableSale(unittest.TestCase):
    '''商品下架'''
    sql1 = "select vg.virtual_goods_id from virtual_goods vg inner join goods g on g.goods_id=vg.goods_id where g.is_on_sale='1' and g.merchant_id='13' and sale_status='normal' and is_delete='0' ;"
    sql2 = "select vg.virtual_goods_id from fbv_sku_warehouse_storage fsws inner join goods_sku gs on gs.sku_id = fsws.sku_id inner join goods g on g.goods_id = gs.goods_id inner join virtual_goods vg on vg.goods_id=g.goods_id where fsws.fbv_warehouse_storage!=0 and g.is_on_sale='1' and g.merchant_id ='13' and g.sale_status='normal';"
    disableSale_url = 'https://m-t1.vova.com.hk/api/v1/product/disableSale'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
    token ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'
    @retry(stop_max_attempt_number=5, wait_random_max=1000)
    def find_productData(self):
        self.con = pymysql.Connect(host='123.206.135.211',
                                   port=3306,
                                   user='vvxxthemis',
                                   password='q3YBGG6JxE67xcYY1s0jIyBY4OmKqhg=',
                                   database='themis')
        return self.con.cursor()

    def test_disableSale1(self):
        '''无海外仓直接下架:token和商品id都正确'''
        cur=self.find_productData()
        cur.execute(self.sql1)
        self.con.commit()
        result=cur.fetchall()

        i = 0
        while i<len(result):
            disableSale_data = {'token': self.token, 'goods_list': result[i]}
            r = requests.post(url=self.disableSale_url, json=disableSale_data, headers=self.headers)
            if r.json()['execute_status'] == 'failed':
                i += 1
                continue
            else:
                print(r.json())
                print('下架的商品id:%s' % disableSale_data['goods_list'])
                self.assertEqual(r.json()['execute_status'], 'success')
                break

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
        cur=self.find_productData()
        cur.execute(self.sql2)
        self.con.commit()
        result=cur.fetchall()

        i = 0
        while i<len(result):
            disableSale_data = {'token': self.token, 'goods_list':result[i],'fbv_disable_way':'disable'}
            r = requests.post(url=self.disableSale_url, json=disableSale_data, headers=self.headers)
            if r.json()['execute_status'] == 'failed':
                i += 1
                continue
            else:
                print(r.json())
                print('下架的商品id:%s' % disableSale_data['goods_list'])
                self.assertEqual(r.json()['execute_status'], 'success')
                break
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
    DisableSale().test_disableSale3()
