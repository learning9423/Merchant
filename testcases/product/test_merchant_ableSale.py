import unittest
import pymysql
from pip._vendor import requests
from retrying import retry


class AbleSale(unittest.TestCase):
    '''商品上架'''
    sql = "select vg.virtual_goods_id from virtual_goods vg inner join goods g on g.goods_id=vg.goods_id where g.is_on_sale='0' and g.merchant_id='13' and g.is_delete='0';"
    ableSale_url = 'https://m-t1.vova.com.hk/api/v1/product/enableSale'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
    token ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'
    @retry(stop_max_attempt_number=5,wait_random_max=1000)
    def find_productId(self):
        self.con = pymysql.Connect(host='123.206.135.211',
                                   port=3306,
                                   user='vvxxthemis',
                                   password='q3YBGG6JxE67xcYY1s0jIyBY4OmKqhg=',
                                   database='themis')
        return  self.con.cursor()

    def test_ableSale1(self):
        '''token和商品id都正确'''
        cur=self.find_productId()
        cur.execute(self.sql)
        self.con.commit()
        result=cur.fetchall()
        i=0
        while i<len(result):
            ableSale_data = {'token': self.token, 'goods_list':result[i]}
            r = requests.post(url=self.ableSale_url, json=ableSale_data, headers=self.headers)
            if r.json()['execute_status'] =='failed':
                i+=1
                continue
            else:
                print(r.json())
                print('上架的商品id:%s'%ableSale_data['goods_list'])
                self.assertEqual(r.json()['execute_status'],'success')
                break

    def test_ableSale2(self):
        '''商品id错误'''

        ableSale_data = {'token': self.token, 'goods_list': [124]}

        r = requests.post(url=self.ableSale_url, json=ableSale_data, headers=self.headers)
        print(r.json())
        self.assertEqual(r.json()['data']['errors_list'][0]['code'],41001)

    def test_ableSale3(self):
        '''token错误'''
        cur=self.find_productId()
        cur.execute(self.sql)
        self.con.commit()
        result=cur.fetchall()
        token = 'e'
        ableSale_data = {'token': token, 'goods_list': result[0]}

        r = requests.post(url=self.ableSale_url, json=ableSale_data, headers=self.headers)
        print(r.json())
        self.assertEqual(r.text, '"Token error"')
        self.assertEqual(r.status_code, 401)


if __name__ == '__main__':
    AbleSale().test_ableSale1()