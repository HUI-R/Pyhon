# 第一页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname: 昆明
# pid: 
# pageIndex: 1
# pageSize: 10

# 第二页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname: 昆明
# pid: 
# pageIndex: 2
# pageSize: 10

import urllib.request
import urllib.parse

def create_request(page):
    base_url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    
    data= {
    'cname': '昆明',
    'pid':'',
    'pageIndex':page,
    'pageSize': '10'
    }

    data= urllib.parse.urlencode(data).encode('utf-8')

    headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36 Edg/103.0.1264.62'
    }

    request=urllib.request.Request(url=base_url,headers=headers,data=data)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open('kfc_' + str(page) + '.json','w',encoding='utf-8')as fp:
        fp.write(content) 


if __name__ == '__main__':
    start_page=int(input('请输入起始页码：'))
    end_page=int(input('请输入结束页码：'))
    
    for page in range(start_page,end_page+1):
        #请求对象定制
        request = create_request(page)
        #获取网页源码
        content = get_content(request)
        #下载数据
        down_load(page,content)