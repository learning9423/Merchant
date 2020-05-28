import unittest
import requests

class LoginOut(unittest.TestCase):
    out_url='https://m-t1.vova.com.hk/index.php?q=admin/main/index/logout'
    headers={'Content-Type':'text/html;charset=utf-8','Authorization':'Basic bGViYmF5OnBhc3N3MHJk'}
    def test_login_out(self):
        '''商家后台退出'''
        r=requests.get(url=self.out_url,headers=self.headers,allow_redirects=False)
        self.assertEqual(r.status_code,302)
        print(r.status_code)

if __name__ == '__main__':
    LoginOut().test_login_out()
