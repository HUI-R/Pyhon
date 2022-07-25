#import urllib.request

# urlencode 应用场景：多个参数的时候

# https://www.baidu.com/s?wd=周杰伦&sex=男

# data = {
#    'wd': '周杰伦',
#   'sex': '男',
#  'location': '中国台湾省'
# }

#a = urllib.parse.urlencode(data)
# print(a)


# 获取https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7的网页源码

import urllib.request
import urllib.parse

base_url = 'http://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}

new_data = urllib.parse.urlencode(data)

# 请求资源路径
url = base_url+new_data

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发出请求
response = urllib.request.urlopen(request)

# 获取网页源码的数据
content = response.read().decode('utf-8')

# 打印数据
print(content)
