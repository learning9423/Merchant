
from common.read_excel import ReadExcel
from pip._vendor import requests


class SendRequest():
    '''请求模板'''

    def sendRequest(s, api_data):

        method = api_data['method']
        url = api_data['url']

        if api_data['params'] == '':
            par = None
        else:
            par = eval(api_data['params'])
        if api_data['headers'] == '':
            header = None
        else:
            header = eval(api_data['headers'])
        if api_data['body'] == '':
            body = None
        else:
            body = api_data['body']

        # 参数请求
        r = s.request(url=url, method=method, headers=header, params=par, data=body,allow_redirects=False)

        return r


if __name__ == '__main__':
    s = requests.session()
    login_data = ReadExcel().readExcel(r'../data/login_api.xlsx', 'Sheet1')
    r=SendRequest.sendRequest(s,login_data[1])
    print(r.json())
