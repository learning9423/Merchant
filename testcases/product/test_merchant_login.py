import requests
import unittest

class TestLogin(unittest.TestCase):
    login_url='https://m-t1.vova.com.hk/index.php?q=admin/main/index/login'
    headers={'Content-Type':'application/x-www-form-urlencoded','Authorization':'Basic bGViYmF5OnBhc3N3MHJk'}

    def test_login1(self):
        '''用户名和密码都正确'''
        login_data={'acct':'yzhang','pswd':'Lb123456','H_sbmt':'yes'}
        r=requests.post(url=self.login_url,data=login_data,headers=self.headers)
        print(r.json())
        self.assertEqual(r.json()['code'],'SUCCESS')

    def test_login2(self):
        '''用户名密码都错误'''
        login_data={'acct':'yzhan','pswd':'LB123456','H_sbmt':'yes'}
        r=requests.post(url=self.login_url,data=login_data,headers=self.headers)
        print(r.json())
        self.assertEqual(r.json()['code'],'ERROR')

    def test_login3(self):
        '''用户名正确密码错误'''
        login_data={'acct':'yzhang','pswd':'LB123456','H_sbmt':'yes'}
        r=requests.post(url=self.login_url,data=login_data,headers=self.headers)
        print(r.json())
        self.assertEqual(r.json()['code'],'ERROR')

    def test_login4(self):
        '''用户名错误密码正确'''
        login_data={'acct':'yzhan','pswd':'Lb123456','H_sbmt':'yes'}
        r=requests.post(url=self.login_url,data=login_data,headers=self.headers)
        print(r.json())
        self.assertEqual(r.json()['code'],'ERROR')

    def test_login5(self):
        '''用户名密码为空'''
        login_data={'acct':'','pswd':'','H_sbmt':'yes'}
        r=requests.post(url=self.login_url,data=login_data,headers=self.headers)
        print(r.json())
        self.assertEqual(r.json()['code'],'ERROR')

if __name__ == '__main__':
    TestLogin().test_login1()


