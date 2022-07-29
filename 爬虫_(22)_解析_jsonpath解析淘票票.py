
import urllib.request

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1659105388183_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    #':authority':' dianying.taobao.com',
    #':method':' GET',
    #':path':' /cityAction.json?activityId&_ksTS=1659105388183_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    #':scheme':' https',
    'accept':' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    #'accept-encoding':' gzip, deflate, br',
    'accept-language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'bx-v':' 2.2.0',
    'cookie':' t=b2cc5abfb55e884334195922051b02f3; cookie2=11c89e1ee6246b049e61ce6b8f5151a5; v=0; _tb_token_=e415085718b40; xlly_s=1; cna=As9qG93ioFgCAXWISPmT6phS; tfstk=cpMAB29oGUY05qVQ1mdu_QuO4mxlZGjTSMUOBAyEgwDRhVWOiSHnpG7H9lzUk3C..; l=eBL9aO-rL5W3mo5MBO5Zourza77t1QAb8sPzaNbMiInca1yh9F9F4NCHmxxXWdtjgtCX0etyac9IRdCh33ji5c0c07kqm0RqExJO.; isg=BGNjVJxaBanRcMmdZPEL4Cuh8qcNWPeaigOB1JXC2kI51IL2HSj36i5KzqRa9E-S',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua':' " Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile':' ?0',
    'sec-ch-ua-platform':' "Windows"',
    'sec-fetch-dest':' empty',
    'sec-fetch-mode':' cors',
    'sec-fetch-site':' same-origin',
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request) 

content = response.read().decode('utf-8')

#split 切割
content = content.split('(')[1].split(')')[0]

with open('爬虫_(22)_解析_jsonpath解析淘票票.json','w',encoding='utf-8')as fp:
    fp.write(content)

import json
import jsonpath

obj = json.load(open('爬虫_(22)_解析_jsonpath解析淘票票.json','r',encoding='utf-8'))

city_list = jsonpath.jsonpath(obj,'$..regionName')

print(city_list)