import requests

from lxml import etree
import time

count = 1
pn = 0

for i in range(9):
    url = f'https://tieba.baidu.com/f?kw=%E7%81%AB%E5%BD%B1%E5%BF%8D%E8%80%85&ie=utf-8&pn={pn}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    }

    response = requests.get(url,headers = headers)

    # 休眠两秒
    time.sleep(2)
    print(response)


    e = etree.HTML(response.text)

    infos = e.xpath('//ul/li/a/img/@bpic')

    # print(infos)

    for info in infos:
        response = requests.get(info,headers = headers)

        time.sleep(0.5)

        with open('./xpath百度贴吧图片/'+str(count)+'.jpg','wb') as fp:
            fp.write(response.content)

        print(f'第{count}张图片下载完毕!')
        count += 1
    pn += 50

print("下载完毕!!!")
