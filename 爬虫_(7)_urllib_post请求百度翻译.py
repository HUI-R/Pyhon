# post请求

import json
import urllib.request

url = 'https://fanyi.baidu.com/langdetect'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}

data = {
    'kw': 'spider'        #?!?!?!?!?!?!?!?!?
}

# post请求的参数必须进行编码  .encode('utf-8')
data = urllib.parse.urlencode(data).encode('utf-8')

# post的请求参数，是不会拼接到URL的后面的  而是需要放在请求对象定制的参数中的
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取相应的数据
content = response.read().decode('utf-8')

# 字符串————>json对象
#import json

obj = json.loads(content)
print(obj)


# post请求方式的参数必须编码     data = urllib.parse.urlencode(data)
# 编码之后  必须调用encode方法   data = urllib.parse.urlencode(data).encode('utf-8')
# 参数是放在请求对象定制的方法中  request=urllib.request.Request(url=url,data=data, headers=headers)
