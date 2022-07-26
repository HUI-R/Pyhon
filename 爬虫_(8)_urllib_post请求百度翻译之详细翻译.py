import json
import urllib.request

url = ' https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    #'Accept':' */*',
    #'Accept-Encoding':' gzip, deflate, br',
    #'Accept-Language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #'Connection':' keep-alive',
    #'Content-Length':' 135',
    #'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BAIDUID=00E8ACC840D9DEDDE0C1EB9A21D147E5:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1651845023; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1651845023; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_NDFlMzRmODA1YjE3YjM1YWNlM2QzMWRhNGU0NDVmZGY1MzYxMTM3MTBmNWE3NmNhMWRiM2U5YjcwMjcyNjhiNjViZWNlMTUyMWVmZWEzMGIxYjNjZDcyYWM3NzJmMDFmODZhNmYyMjNjYWQ4NjNiZTBkM2MzMzQ5Mzg4MmJlNjk1ODYxZGJmOGJkYzZiNzVkZWM0MDE1Yzg0ZmQxNGY0YQ=='
    #'Host':' fanyi.baidu.com',
    #'Origin: https':'//fanyi.baidu.com',
    #'Referer: https':'//fanyi.baidu.com/',
    #'sec-ch-ua':' " Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
    #'sec-ch-ua-mobile':' ?1',
    #'sec-ch-ua-platform':' "Android"',
    #'Sec-Fetch-Dest':' empty',
    #'Sec-Fetch-Mode':' cors',
    #'Sec-Fetch-Site':' same-origin',
    #'User-Agent':' Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36 Edg/101.0.1210.32',
    #'X-Requested-With':' XMLHttpRequest'
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '41ad4ac51fdc1b04765c53db6f634846',
    'domain': 'common'
}
# post请求的参数  必须进行编码  并且调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象的定制
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求 
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

#import json
obj = json.loads(content)
print(obj)
