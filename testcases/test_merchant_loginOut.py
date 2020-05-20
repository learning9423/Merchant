import unittest
import requests

class LoginOut(unittest.TestCase):

    def test_login_out(self):
        url='https://m-t2.vova.com.hk/index.php?q=admin/main/index/logout'
        headers={'Content-Type':'application/x-www-form-urlencoded','Authorization':'Basic bGViYmF5OnBhc3N3MHJk'}
        r=requests.post(url=url,headers=headers,allow_redirects=False)
        self.assertEqual(r.status_code,302)
        print(r.json())
