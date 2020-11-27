import random
import time

from pip._vendor import requests


def test1():
    url = "https://merchant.vova.com.hk/api/v1/product/uploadGoods"
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic bGViYmF5OnBhc3N3MHJk'}
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTc4MTgxNjIsInNjb3BlIjpbImdldCIsInBvc3QiXSwidWlkIjoiMTMiLCJ1TmFtZSI6InRlc3QifQ.ojD-GOE1eBH_pEqBwhBOuHlbfgpmnE1VljoR9bSRDNg'

    data = {
        "token": token,
        "items": [{
            "cat_id": "5872",
            "parent_sku": "w1" + str(random.randint(0, 100000)),
            "goods_sku": "tt",
            "goods_name": "avg",
            "storage": 12,
            "goods_description": "att G9",
            "tags": "",
            "goods_brand": "",
            "market_price": 22,
            "shop_price": 23,
            "shipping_fee": 2,
            "shipping_weight": 1,
            "shipping_time": "",
            "from_platform": "",
            "style_size": "400",
            "style_color": "green",
            "style_quantity": "200",
            "main_image": "http://img.gaoxiaogif.com/d/file/201908/8ae30f4f63595bd2db1bf0a21333979a.gif",
            "extra_image": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1582721500794&di=752f1e2ed42e10b0a6656f60a0270727&imgtype=0&src=http%3A%2F%2Fimages.liqucn.com%2Fimg%2Fh61%2Fh86%2Fimg_localize_fe2f4997a746a0befedbfac7b8370f3d.jpg"

        }],
        "ignore_warning": "1"
    }

    r = requests.post(url=url, headers=headers, json=data)
    print(r.json())


if __name__ == '__main__':
    a = (1)
    print(''.join(a))
