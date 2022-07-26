#需求 使用handler访问百度    获取网页源码


import urllib.request

url='http://www.baidu.com'

headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36 Edg/103.0.1264.62'
}

request = urllib.request.Request(url=url,headers=headers)

#handler  build_opener  open

# (1)获取handler对象
handler = urllib.request.HTTPHandler()  

# (2)获取opener对象
opener = urllib.request.build_opener(handler)

# (3)调用open方法
response = opener.open(request)

content =response.read().decode('utf-8')

print(content)