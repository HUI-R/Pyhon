
from bs4 import BeautifulSoup

# 通过解析本地文件  讲解bs4的基础语法
# 默认打开的文件的编码格式是gbk  所以打开文件的时候需要指定编码
soup = BeautifulSoup(open('爬虫_(23)_解析_bs4的基本使用.html',encoding='utf-8'),'lxml')

# #根据标签名查找节点
# #找到的是第一个符合条件的数据
# print(soup.a)
# #获取标签的属性和属性值
# print(soup.a.attrs)

# bs4的一些函数
# (1)find

#   返回第一个符合条件的数据
# print(soup.find('a'))

#   根据title的值来找到对应的标签对象
# print(soup.find('a',title="a2"))

#   根据class的值来找到对应的标签对象   注意的是class需要添加下划线(特殊字符)
# print(soup.find('a',class_="a1"))


# (2)find_all

#   返回的是一个列表 并且返回了所有的a标签
# print(soup.find_all('a'))

# 如果先返回的是多个标签的数据 那么需要在find_all的参数中添加的是列表数据
# print(soup.find_all(['a','span']))

# limit的作用是查找前几个的数据
# print(soup.find_all('li',limit=2))


# (3)select 

#   select方法返回的是一个列表  并且会返回多个数据
# print(soup.select('a'))

#   可以通过 . 代表class    我我们把这种操作叫做类选择器
# print(soup.select('.a1'))

# print(soup.select('#l1'))

# 属性选择器--通过属性来寻找对应的标签
#   查找到l1标签中有id的标签
# print(soup.select('li[id]'))

#   查找到li标签中id为l2的标签
# print(soup.select('li[id="l2"]'))

# 层级选择器
#   后代选择器
#   找到的是div下的li
# print(soup.select('div li'))

#   子代选择器
#   某标签的第一级字标签
#   注意：很多的计算机编程语言中 如果不加空格会报错 但是在bs4中不会报错 会显示内容
# print(soup.select('div > ul > li'))

# 找到a标签和li标签的所有的对象
# print(soup.select('a,li'))


# 节点信息
#   获取节点内容
obj=soup.select('#d1')[0]
# 如果标签对象中 只有内容 那么string和get_text()都可以使用
# 如果标签对象中 除了内容还有标签 那么string就获取不到数据 而get_text()是可以获取数据的
# 我们一般情况下 推荐使用get_text()
# print(obj.string)
# print(obj.get_text())


# 节点的属性
# name是标签的名字
# obj=soup.select('#p1')[0]
# 将属性值作为一个字典值返回
# print(obj.attrs)

#获取节点的属性
obj=soup.select('#p1')[0]

print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])



