import requests
import re
import time
pn = 0
count = 1
for i in range(9):
    url = f'https://wenku.baidu.com/view/1d7bc60a5bfafab069dc5022aaea998fcc224098.html?_wkts_=1700305461447&bdQuery=2023%E5%9B%9B%E7%BA%A7%E6%A0%B8%E5%BF%83%E8%AF%8D%E6%B1%87700%E4%B8%AA'


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