import requests
from bs4 import BeautifulSoup
import time

count = 1
pn = 0

for i in range(9):
    url = f'https://tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn={pn}'

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
        }

    response = requests.get(url,headers = headers)

    time.sleep(2)
    print(response)
    bs = BeautifulSoup(response.text,'lxml')

    a_list = bs.find_all('a',class_ = 'thumbnail vpic_wrap')

    for a in a_list:
        img = a.find('img')
        bpic = img.get('bpic') if img else None

        response = requests.get(bpic,headers = headers)
        time.sleep(0.1)

        with open('./bs4百度贴吧图片/'+str(count)+'.jpg','wb') as fp:
            fp.write(response.content)

        print(f'第{count}张照片下载成功!!!')
        count += 1

    pn += 50

print("下载完毕!!!")
