import unittest

import pymysql
from retrying import retry


class UpdateRegionShippingFee(unittest.case):
    updateRegionShippingFee_url='https://m-t1.vova.com.hk/api/v1/product/updateRegionShippingFee'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
    sql="select old_goods_id from goods where merchant_id='13' and is_on_sale='1' and is_delete='0'"

    @retry(stop_max_attempt_number=5,wait_random_max=1000)
    def find_productData(self):
        self.con = pymysql.Connect(host='123.206.135.211',
                                   port=3306,
                                   user='vvxxthemis',
                                   password='q3YBGG6JxE67xcYY1s0jIyBY4OmKqhg=',
                                   database='themis')
        return self.con.cursor()

    def test_updateRegionShippingFee(self):
        cur=self.find_productData()
        cur.execute(self.sql)

        result=cur.fetchall()
        token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'
        updateRegionShippingFee_data={'token':token, "update_info": [{"parent_sku": result[0],"region_fee": {'CA':2,'AU':3}}]}

