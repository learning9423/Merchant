import random
import re

from pip._vendor import requests


class spider():
    url_lol = 'https://www.huya.com/g/lol'
    root_pattern = r'<li class="game-live-item" gid="1" data-lp="[\d]*">([\s\S]*?)</li>' #正则根路径
    name_pattern=r'<i class="nick" title="[\s\S]*">([\s\S]*?)</i>'
    num_pattern=r'<i class="js-num">([\s\S]*?)</i>'

    def spider_lol(self):
        '''获取网页信息'''
        html = requests.post(url=self.url_lol)
        html = html.text
        return html

    def analysis(self, html):
        '''提取人名和人数'''
        anchor_html = re.findall(self.root_pattern,html)
        anchors=[]
        for anch in anchor_html:
            name=re.findall(self.name_pattern,anch)
            num=re.findall(self.num_pattern,anch)
            anchor={"name":name,"num":num}
            anchors.append(anchor)
        print(anchors)
    def go(self):
        html = self.spider_lol()
        self.analysis(html)


if __name__ == '__main__':
    spider().go()
