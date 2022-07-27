
# 获取网页的源码
# 解析   解析的服务器响应的文件  etree.HTML
# 打印

import urllib.request

url="http://www.baidu.com"

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
}

#请求对象定制
request = urllib.request.Request(url=url,headers=headers)

#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

#获取网页源码
content = response.read().decode('utf-8')

#解析网页源码 来获取我们想要的数据
from lxml import etree 

#解析服务器响应文件
tree = etree.HTML(content)

#获取响应的数据
result = tree.xpath('//input[@id="su"]/@value')

print(result)