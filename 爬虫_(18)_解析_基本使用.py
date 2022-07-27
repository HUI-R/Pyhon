from lxml import etree

# xpath解析
# (1)本地文件                                                  etree.parse
# (2)服务器响应文件   response.read().decode('utf-8') *****     etree.HTML()

# xpath解析本地文件
tree = etree.parse('爬虫_(18)_解析_基本使用.html')

# tree.xpath('xpath路径')


# 路径查询
#    '//':查找所有子孙结点,不考虑层级关系
#    '/ ':找直接子节点 
# 查找ul里的li
# li_list = tree.xpath('//body//li')
# =li_list = tree.xpath('//body/ul/li')

# 内容查询
#    '//div/h1/text()'
# 查找所有有id属性的li标签
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')

# 属性查询
#   '//@class'
# 谓词查询
#     '//div[@id]' 
#     '//div[@id="maincontent"]'
# 查找到id为l1的li标签的class的属性值
# li = tree.xpath('//ul/li[@id="l1"]/@class')


#模糊查询
#   '//div[contains(@id,"he")]
#   '//div[starts-with(@id,"he")]
#查询id中包含li的标签
# li_list = tree.xpath('//ul/li[contains(@id,"li")]/text()')
#查询id的值以l开头的li标签
# li_list = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')


#逻辑查询
#    '//div[@id="head" and @class="s_down"]'
#    '//title | //price'
#查询id为l1和class为c1的标签
#li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')

li_list = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')

# 判断列表的长度
print(li_list)
print(len(li_list))
