# 适应的场景：采集数据的时候，需要绕过登录，然后进入到某个页面 
# 个人信息界面是utf-8  但是还是报错了编码错误  因为没有进入到个人信息页面  而是跳转到了登录页面
# 那么登录页面不是utf-8，所以报错

import urllib.request

url = 'https://weibo.cn/5676349390/info'

# 
headers = {
    #':authority':' weibo.cn',
    #':path':' /5676349390/info',
    #':scheme':' https',
    'accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # #accept-encoding':' gzip, deflate, br',
    'accept-language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control':' max-age=0',
    # cookie中携带着你的登录信息  如果有登录后的cookie  那么我们就可以携带着cookie进入到任何页面
    'cookie':' _T_WM=e4a9fd0c6f017b85d2c74864a5cef8f1; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW-QE4z0ej0x-PUmAokZmrB5NHD95QfSoMce0B4e0.7Ws4DqcjHi--ciKn0iKyWi--RiKLFi-z7C8Hi; SUB=_2A25P34aiDeRhGeNI7FQS9CfPwjyIHXVtIyrqrDV6PUJbktANLVqjkW1NSCZWSU7arjWG4xPQcjz3SfPFsdSV_qTc; SSOLoginState=1658582770',
    #referer  判断当前路径是不是由上一个路径进来的   一般情况下是做图片的防盗链
    'referer':'https://weibo.cn/',
    'sec-ch-ua':' " Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile':' ?0',
    'sec-ch-ua-platform':' "Windows"',
    'sec-fetch-dest':' document',
    'sec-fetch-mode':' navigate',
    'sec-fetch-site':' same-origin',
    'sec-fetch-user':' ?1',
    'upgrade-insecure-requests':' 1',
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
}

#请求对象定制
request = urllib.request.Request(url = url,headers = headers)
# 模拟浏览器向服务器发送请求 
response = urllib.request.urlopen(request)
#获取响应数据
content = response.read().decode('utf-8')

#将数据保存到本地
with open('weibo.html','w',encoding='utf-8')as fp:
    fp.write(content)