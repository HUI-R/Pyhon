#  https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

# 需求  获取 https://www.baidu.com/s?wd=周杰伦 的网页源码

import urllib.request


url = 'https://www.baidu.com/s?wd='

# 请求对象的定制为了解决反爬的一种手段
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}

# 将 周杰伦 三个变成unicode编码的格式
# 我们需要依赖于urllib.parse
name = urllib.parse.quote('周杰伦')

url = url+name

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)


# 模拟服务器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应内容
content = response.read().decode('utf-8')

# 打印数据
print(content)
