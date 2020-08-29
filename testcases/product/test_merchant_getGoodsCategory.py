import unittest
from pip._vendor import requests


class GetGoodsCategory(unittest.TestCase):
    '''获取最新分类id信息'''
    getGoodsCategory_url = 'https://m-t1.vova.com.hk/api/v1/product/getGoodsCategory'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
    token ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'

    def test_getGoodsCategory1(self):
        '''token正确'''
        getGoodsCategory_data={'token':self.token}
        r=requests.get(url=self.getGoodsCategory_url,headers=self.headers,params=getGoodsCategory_data)
        print(r.json())
        self.assertEqual(r.json()['execute_status'],'success')

    def test_getGoodsCategory2(self):
        '''token不正确'''
        token ='e'
        getGoodsCategory_data={'token':token}
        r=requests.get(url=self.getGoodsCategory_url,headers=self.headers,params=getGoodsCategory_data)
        print(r.json())
        self.assertEqual(r.json(),'Token error')



if __name__ == '__main__':
    GetGoodsCategory().test_getGoodsCategory1()