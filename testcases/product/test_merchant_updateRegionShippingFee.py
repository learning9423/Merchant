import unittest
import pymysql
from pip._vendor import requests
from retrying import retry

class UpdateRegionShippingFee(unittest.TestCase):
    '''更新国家运费'''
    updateRegionShippingFee_url='https://m-t1.vova.com.hk/api/v1/product/updateRegionShippingFee'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
    sql="select old_goods_id from goods where merchant_id='13' and is_on_sale='1' and is_delete='0'"
    token ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'
    @retry(stop_max_attempt_number=5,wait_random_max=1000)
    def find_productData(self):
        self.con = pymysql.Connect(host='123.206.135.211',
                                   port=3306,
                                   user='vvxxthemis',
                                   password='q3YBGG6JxE67xcYY1s0jIyBY4OmKqhg=',
                                   database='themis')
        return self.con.cursor()

    def test_updateRegionShippingFee1(self):
        '''token与运费参数都正确'''
        cur=self.find_productData()
        cur.execute(self.sql)
        result=cur.fetchone()
        updateRegionShippingFee_data={'token':self.token, 'update_info': [{'parent_sku':result[0],'region_fee': {'CA':2,'AU':16}}]}

        r=requests.post(url=self.updateRegionShippingFee_url,headers=self.headers,json=updateRegionShippingFee_data)
        print(r.json())
        self.assertEqual(r.json()['execute_status'], 'success')

    def test_updateRegionShippingFee2(self):
        '''token错误，运费参数正确'''
        cur=self.find_productData()
        cur.execute(self.sql)
        result=cur.fetchone()
        token='e'
        updateRegionShippingFee_data={'token':token, 'update_info': [{'parent_sku':result[0],'region_fee': {'CA':2,'AU':16}}]}

        r=requests.post(url=self.updateRegionShippingFee_url,headers=self.headers,json=updateRegionShippingFee_data)
        print(r.json())
        self.assertEqual(r.json(), 'Token error')

    def test_updateRegionShippingFee3(self):
        '''token正确，运费参数不正确'''
        updateRegionShippingFee_data={'token':self.token, 'update_info': [{'parent_sku':'e','region_fee': {'CA':2,'AU':16}}]}

        r=requests.post(url=self.updateRegionShippingFee_url,headers=self.headers,json=updateRegionShippingFee_data)
        print(r.json())
        self.assertEqual(r.json()['execute_status'], 'failed')
        self.assertEqual(r.json()['message'], '第[0]组数据parent_sku(e)不存在')

if __name__ == '__main__':
    UpdateRegionShippingFee().test_updateRegionShippingFee3()