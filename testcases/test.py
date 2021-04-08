import random
import re

from pip._vendor import requests


class spider():
    url_lol = 'https://www.huya.com/g/lol'
    root_pattern = r'<li class="game-live-item" gid="1" data-lp="5668003">([\s\S]*?)</li>' #正则根路径

    def spider_lol(self):
        '''获取网页信息'''
        html = requests.post(url=self.url_lol)
        html = html.text
        return html

    def analysis(self, html):
        '''提取人名和人数'''
        r = re.findall(self.root_pattern,html)
        print(r)

    def go(self):
        html = self.spider_lol()
        self.analysis(html)


if __name__ == '__main__':
    spider().go()
