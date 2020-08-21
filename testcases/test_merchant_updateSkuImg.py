import unittest
import pymysql
from pip._vendor import requests
from retrying import retry


class UpdateSkuImg(unittest.TestCase):
    updateSkuImg_url='https://m-t1.vova.com.hk/api/v1/product/updateSkuImg'
    headers={'Content-Type':'application/x-www-form-urlencoded','Authorization':'Basic bGViYmF5OnBhc3N3MHJk'}
    sql1="select vg.virtual_goods_id,gs.pdd_sku,gs.img_id from virtual_goods vg inner join goods_sku gs on vg.goods_id = gs.goods_id " \
        "inner join goods g on g.goods_id=gs.goods_id where g.is_delete ='0' and merchant_id='13' and g.goods_sn like 'SN%' and g.is_on_sale='1';"
    sql2="select vg.virtual_goods_id,gs.pdd_sku,gs.img_id from virtual_goods vg inner join goods_sku gs on vg.goods_id = gs.goods_id " \
        "inner join goods g on g.goods_id=gs.goods_id where g.is_delete ='0' and merchant_id='13' and g.goods_sn like 'GSN%' and g.is_on_sale='1';"
    @retry(stop_max_attempt_number=5,wait_random_max=1000)
    def find_productData(self):
        self.con = pymysql.Connect(host='123.206.135.211',
                                   port=3306,
                                   user='vvxxthemis',
                                   password='q3YBGG6JxE67xcYY1s0jIyBY4OmKqhg=',
                                   database='themis')
        return self.con.cursor()

    def test_updateSkuImg1(self):
        '''参数不为空，参数有效'''
        cur=self.find_productData()
        cur.execute(self.sql1)
        self.con.commit()

        result=cur.fetchall()
        token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'
        updateSkuImg_data={'token':token,'product_id':result[0][0],'sku_img_info':[{'goods_sku':result[0][1],'img_id':str(result[0][2])}]}

        r=requests.post(url=self.updateSkuImg_url,headers=self.headers,json=updateSkuImg_data)
        print(r.json())
        print('更新的商品信息为：%s'%updateSkuImg_data['product_id'],updateSkuImg_data['sku_img_info'])
        self.assertEqual(r.json()['execute_status'], 'success')
        self.assertEqual(r.json()['data']['code'] ,20000)

    def test_updateSkuImg2(self):
        '''克隆商品不能更新图片'''
        cur=self.find_productData()
        cur.execute(self.sql2)
        self.con.commit()

        result=cur.fetchall()
        token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'
        updateSkuImg_data={'token':token,'product_id':result[0][0],'sku_img_info':[{'goods_sku':result[0][1],'img_id':str(result[0][2])}]}

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
        token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'

        for i in range(3):
             if i==0:
                updateSkuImg_data={'token':token,'product_id':'','sku_img_info':[{'goods_sku':result[0][1],'img_id':str(result[0][2])}]}
                r=requests.post(url=self.updateSkuImg_url,headers=self.headers,json=updateSkuImg_data)
                print(r.json())
                self.assertEqual(r.json()['execute_status'], 'failed')
                self.assertEqual(r.json()['data']['code'] ,40001)
             elif i==1:
                updateSkuImg_data={'token':token,'product_id':result[0][0],'sku_img_info':[{'goods_sku':'a','img_id':str(result[0][2])}]}
                r=requests.post(url=self.updateSkuImg_url,headers=self.headers,json=updateSkuImg_data)
                print(r.json())
                self.assertEqual(r.json()['execute_status'], 'failed')
                self.assertEqual(r.json()['data']['errors_list'][0]['code'] ,41020)
             elif i==2:
                updateSkuImg_data={'token':token,'product_id':result[0][0],'sku_img_info':[{'goods_sku':result[0][1],'img_id':'a1'}]}
                r=requests.post(url=self.updateSkuImg_url,headers=self.headers,json=updateSkuImg_data)
                print(r.json())
                self.assertEqual(r.json()['execute_status'], 'failed')
                self.assertEqual(r.json()['data']['errors_list'][0]['code'] ,41021)
    def test_updateSkuImg4(self):
        '''参数不为空，参数有效'''
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
    UpdateSkuImg().test_updateSkuImg3()