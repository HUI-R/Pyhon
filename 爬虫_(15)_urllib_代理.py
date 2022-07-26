import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers ={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36 Edg/103.0.1264.62'
}

#请求对象定制
request = urllib.request.Request(url=url,headers=headers)\

#模拟浏览器访问服务器
#response = urllib.request.urlopen(request)

proxies={
    'http':'61.160.236.33:3129'
}

# hanlder  build_opener  open
handler = urllib.request.ProxyHandler(proxies = proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

#获取响应的信息
content = response.read().decode('utf-8')

#保存到本地
with open('daili.html','w',encoding='utf-8')as fp:
    fp.write(content)