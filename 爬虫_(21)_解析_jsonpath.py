#xpath与json的区别对比：https://blog.csdn.net/Obstinate_L/article/details/125294971

import json
import jsonpath

obj = json.load(open('爬虫_(21)_解析_jsonpath.json','r',encoding='utf-8'))


# 书店所有书的作者
# author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')
# print(author_list)

# 所有作者
# author_list = jsonpath.jsonpath(obj,'$..author')
# print(author_list)

# store下面的所有元素
# tag_list = jsonpath.jsonpath(obj,'$.store.*')
# print(tag_list)

# stor里面所有的东西price
# price_list = jsonpath.jsonpath(obj,'$.store..price')
# print(price_list)

# 第三本书
# book = jsonpath.jsonpath(obj,'$..book[2]')
# print(book)

# 最后一本
# book = jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
# print(book) 

# 前两本书
# book = jsonpath.jsonpath(obj,'$..book[0,1]') 
# book = jsonpath.jsonpath(obj,'$..book[:2]')
# print(book)

#条件过滤需要在 （） 的前面添加一个 ？
#过滤出所有包含isbn的书
# book = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
# print(book)

# 哪本书超过了10块钱 
book_list = jsonpath.jsonpath(obj,'$..book[?(@.price>10)]')
print(book_list)