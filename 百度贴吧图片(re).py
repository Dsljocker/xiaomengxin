import requests
import re
import time
pn = 0
count = 1
for i in range(9):
    url = f'https://tieba.baidu.com/f?kw=%E5%A5%A5%E7%89%B9%E6%9B%BC&ie=utf-8&pn={pn}'


    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
        }

    response = requests.get(url = url,headers = headers)
    # 休眠两秒
    time.sleep(2)
    # print(response.text)

    infos = re.findall(r'<a\s[^>]*class="thumbnail vpic_wrap"[^>]*>\s*<img\s+[^>]*bpic="([^"]*)"', response.text)
    # print(infos)
    if len(infos) == 0:
        print('没有数据')
    for info in infos:
        resp =  requests.get(url = info,headers = headers)
        with open('./re百度贴吧图片/'+ str(count) +'.jpg','wb') as fp:
            fp.write(resp.content)
        print(f'第{count}张下载完成')
        count += 1
    pn += 50
print('下载完毕')