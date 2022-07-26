from lxml import etree

# xpath解析
# (1)本地文件                                                  etree.parse
# (2)服务器响应文件   response.read().decode('utf-8') *****     etree.HTML()

tree=etree.parse('爬虫_(18)_解析_基本使用.html')

print(tree)

