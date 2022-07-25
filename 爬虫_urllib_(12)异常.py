
import urllib.request
import urllib.error

# url='https://blog.csdn.net/zhangxia_/article/details/1253551863'

url = 'https://goudan666.com'

headers= {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36 Edg/103.0.1264.62'
    }

try:
    request = urllib.request.Request(url = url,headers = headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')
except urllib.error.HTTPError:
    print('系统正在升级。。。')
except urllib.error.URLError:
    print('我都说了，系统正在升级!!!')


