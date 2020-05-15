import unittest
import requests


class TestLogin(unittest.TestCase):

    def test_login(self):

        login_url='https://m-t1.vova.com.hk/index.php?q=admin/main/index/login'
        # login_header={'Content-Type': 'application/json'}
        user={'acct':'yzhang','pswd':'Lb123456'}




if __name__ == '__main__':
    TestLogin().test_login()