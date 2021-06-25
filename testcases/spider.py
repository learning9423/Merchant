import re
from pip._vendor import requests


class spider():
    url_lol = 'https://www.huya.com/g/lol'
    root_pattern = r'<li class="game-live-item" gid="1" data-lp="[\d]*">([\s\S]*?)</li>'  # 正则根路径
    name_pattern = r'<i class="nick" title="[\s\S]*?">([\s\S]*?)</i>'
    num_pattern = r'<i class="js-num">([\s\S]*?)</i>'

    def spider_lol(self):
        '''获取网页信息'''
        html = requests.post(url=self.url_lol)
        html = html.text
        return html

    def analysis(self, html):
        '''提取人名和人数'''
        anchor_html = re.findall(self.root_pattern, html)
        print(anchor_html.group())
        anchors = []
        for anch in anchor_html:
            name = re.findall(self.name_pattern, anch)
            num = re.findall(self.num_pattern, anch)
            anchor = {"name": str(name), "num": str(num)}
            anchors.append(anchor)
        return anchors

    def modify(self, anchors_any):

        for anchor in anchors_any:
            anchor['name'] = anchor['name'].strip('[\'\']')
            anchor['num'] = anchor['num'].strip(r'[\'"万"\']')  # 去掉中文万
            anchor['num'] = int(float(anchor['num']) * 10000)  # 转化为整数并乘万
        return anchors_any

    def rank(self, anchors_cmp):

        anchors_cmp.sort(key=lambda x: x['num'], reverse=True) #根据观看人数排名
        for anchor in anchors_cmp:
            print('姓名:{}\t观看人数:{}'.format(anchor['name'],anchor['num'],end=''))

    def go(self):
        html = self.spider_lol()
        anchors_any = self.analysis(html)
        anchors_cmp = self.modify(anchors_any)
        self.rank(anchors_cmp)


if __name__ == '__main__':
    spider().go()
