import urllib.request

proxies_pool = [
    { 'http':'58.20.235.180:9091'},
    { 'http':'101.200.127.149:3129'},
    { 'http':'58.20.184.187:9091'},
    { 'http':'61.160.236.33:3129'}
]

import random

proxies = random.choice(proxies_pool)

url = 'http://www.baidu.com/s?wd=ip'

headers ={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36 Edg/103.0.1264.62'
}

request = urllib.request.Request(url=url,headers=headers)

handler = urllib.request.ProxyHandler(proxies = proxies)

opener = urllib.request.build_opener(handler)

response=opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html','w',encoding='utf-8')as fp:
    fp.write(content)