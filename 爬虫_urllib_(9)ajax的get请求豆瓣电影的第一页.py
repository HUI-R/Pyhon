
#get请求
#获取豆瓣电影的第一页数据  并且保存数据

import urllib.request

url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}


#(1)请求对象定制
request = urllib.request.Request(url=url, headers=headers)

#(2)获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

#(3)数据下载到本地
#open方法默认是用的是gbk的编码  如果我们想保存汉字 那么需要在open方法中指定编码格式为utf-8
#encoding='utf-8'

#fp = open('douban.json','w',encoding='utf-8')
#fp.write(content)

with open('douban1.json','w',encoding='utf-8') as fp:
    fp.write(content)