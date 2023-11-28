import requests
from lxml import etree
import time
pn = 0 # 定义pn字段
count = 1
for i in range(9):
    url = f'https://tieba.baidu.com/f?kw=%E8%A7%86%E9%A2%91&ie=utf-8&pn={pn}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
        'Referer':'https://tieba.baidu.com/f?kw=%E8%A7%86%E9%A2%91&ie=utf-8&pn=50'
    }

    datas = {
        'vt': '0',
        'pt': '3',
        'ver': '',
        'cr': '2',
        'cd': '0',
        'sid': '',
        'ft': '2',
        'tbau': '2023-10-29_bc0e013a590546389f75a13266d995cb33778d4f57c59c60685049d939469ed2',
        'ptid': '8044791131'
    }

    response = requests.get(url = url,headers = headers,params = datas)
    # print(response.text)
    time.sleep(2)

    e = etree.HTML(response.text)

    infos = e.xpath('//a/@data-video')
    # print(infos)

    for info in infos:
        response = requests.get(info,headers = headers)

        with open('./xpath百度贴吧视频/'+str(count)+'.mp4','wb') as fp:
            fp.write(response.content)
        print(f'第{count}个视频下载完毕!!!')
        count += 1

    print(f'--------------第{i + 1}页视频下载完毕!!!----------------')
    pn += 50
    time.sleep(0.1)

print('下载完毕!!!')