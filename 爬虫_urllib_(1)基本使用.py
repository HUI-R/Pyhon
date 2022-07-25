# 使用urllib来获取百度首页的源码

import urllib.request  # 允许使用网络连接

url = 'http://www.baidu.com'     # (1)定义一个url 即需要访问的地址

response = urllib.request.urlopen(url)      # (2)模拟浏览器向服务器发送访问请求  response 响应
content = response.read().decode('utf-8')  # (3)获取响应页面的源码   content 内容
# read方法 返回的是字节形式的二进制数据
# 需要将二进制的数据转换为字符串
# 二进制 ——————> 字符串  解码  decode（‘解码的格式’）
print(content)  # (4)打印数据
