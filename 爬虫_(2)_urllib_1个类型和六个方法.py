import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)


# 一个类型和六个方法
# response是HTTPResponse的类型
# print(type(response))

# content是按照一个字节一个字节的去读  x是返回多少个字节
#content = response.read(x)
# print(content)

# readline  读取一行
# readlines 读取全部内容

# 返回状态码  若200即证明逻辑没有错
# print(response.getcode())

# 返回的是url的地址
# print(response.geturl())

# 获取状态信息
# print(response.getheaders())

# 一个类型 HTTPResponse
# 六个方法 read readline readlines getcode geturl getheaders
