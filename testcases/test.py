from pip._vendor import requests


class spider():

    url_open='https://www.huya.com/g/lol'


    def spider_lol(self):

        r=requests.post(url=self.url_open)
        html=r.content
        return html

    def


    def go(self):
        self.spider_lol()


if __name__ == '__main__':
    r=spider()
    r.go()
