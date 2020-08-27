import unittest
import requests

class UploadGoods(unittest.TestCase):
    upload_url='https://m-t1.vova.com.hk/api/v1/product/uploadGoods'
    headers={'Content-Type':'application/x-www-form-urlencoded','Authorization':'Basic bGViYmF5OnBhc3N3MHJk'}
    token ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDEzOTAxNjYsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMSIsInVOYW1lIjoiMjMzIn0.-KEPLW5z7egKrnSIL4UBL5zGdwgzS77Gxi4NNvnxMpo'
    data={}
    def test_uploadGoods1(self):
        token=''
        upload_data={'token':token}
        r=requests.post(url=self.upload_url,json=upload_data,header=self.headers)

