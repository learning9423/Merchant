import requests
import unittest

class TestLogin(unittest.TestCase):

    def test_username_password_true(self):

        login_url='https://m-t1.vova.com.hk/index.php?q=admin/main/index/login'
        headers={'Content-Type':'application/x-www-form-urlencoded','Authorization':'Basic bGViYmF5OnBhc3N3MHJk'}
        cookies={'Cookie': 'VVMTID=rB9Vwl5wM+uvvxf+AwPbAg==; SSTID=idus7p4ttllosgj3asorcb8s1c; _ga=GA1.3.615625698.1588744918; '
                 'VVMTSID=3d4d736de8665bd552bbff4bff42b29a; _gid=GA1.3.2041618890.1589525117'}
        user={'acct':'yzhang','pswd':'Lb123456','H_sbmt':'yes'}
        r=requests.post(url=login_url,data=user,headers=headers)
        print(r.text)

if __name__ == '__main__':
    TestLogin().test_username_password_true()


    # Authorization: Basic bGViYmF5OnBhc3N3MHJk