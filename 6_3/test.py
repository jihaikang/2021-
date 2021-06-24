# from bs4 import BeautifulSoup


# soup = BeautifulSoup('<b class="boldest strikeout">Extremely bold</b>')
# s = soup.b.string
# print(s)        # Extremely bold
# # .attrs以字典的形式返回一个对象 ['class']返回该对象以字符串的形式
# print(soup.b.attrs)  # <class 'bs4.element.NavigableString'>

# 迭代 子节点

# from bs4 import BeautifulSoup
# # import bs4

# if __name__ == '__main__':
#     # 将本地的html文档中的数据加载到该对象中
#     fp = open('6_3\hU.html','r', encoding='utf-8')
#     soup = BeautifulSoup(fp, 'lxml')
#     # print(soup)
#     # page_text = response.text
#     # soup = BeautifulSoup(page_text,'lxml')
#     print(soup.a)  # soup.tagName 返回的是html中第一次出现的tagName标签
#     print('--'*20)
#     print(soup.div)
#     print('--'*20)

#     print(soup.find('div'))  # find(tagName) 等同于 soup.select
#     print('--'*20)
#     print(soup.find('div', class_='song'))  # 属性定位
    # print('--'*20)

    # print(soup.find_all('a'))  # 返回符合要求的所有标签（列表）
    # print('--'*20)

    # print(soup.select('.tang'))  # 返回的是一个列表
    # print('--'*20)
    # # print(soup.select('.tang > ul > li > a')[0]) # 层级选择器   > 表示一个层级
    # print('--'*20)
    # print(soup.select('.tang > ul  a')[0])  # 空格表示多个层级
    # print('--'*20)
    # print(soup.select('.tang > ul  a')[0].text)
    # print('--'*20)
    # print(soup.select('.tang > ul  a')[0].get_text())
    # print('--'*20)
    # print(soup.select('.tang > ul  a')[0].string)
    # print('--'*20)
    # print(soup.select('.tang > ul  a')[0]['href'])
   
# from bs4 import BeautifulSoup
# html = """
# <html>
# <head><title>标题</title></head>
# <body>
#  <p class="title" name="dromouse"><b>标题</b></p>
#  <div name="divlink">
#   <p>
#    <a href="http://example.com/1" class="sister" id="link1">链接1</a>
#    <a href="http://example.com/2" class="sister" id="link2">链接2</a>
#    <a href="http://example.com/3" class="sister" id="link3">链接3</a>
#   </p>
#  </div>
#  <p></p>
#  <div name='dv2'></div>
# </body>
# </html>
# """
# soup = BeautifulSoup(html, 'lxml')
# # 通过tag查找
# # print(soup.select('title'))             # [<title>标题</title>]

# # 通过tag逐层查找
# # print(soup.select("html head title"))   # [<title>标题</title>]

# # 通过class查找
# # print(soup.select('.sister'))
# # [<a class="sister" href="http://example.com/1" id="link1">链接1</a>,
# # <a class="sister" href="http://example.com/2" id="link2">链接2</a>,
# # <a class="sister" href="http://example.com/3" id="link3">链接3</a>]

# # 通过id查找
# # print(soup.select('#link1, #link2'))
# # [<a class="sister" href="http://example.com/1" id="link1">链接1</a>,
# # <a class="sister" href="http://example.com/2" id="link2">链接2</a>]

# # 组合查找
# # print(soup.select('p #link1'))# [<a class="sister" href="http://example.com/1" id="link1">链接1</a>]

# # 查找直接子标签
# # print(soup.select("head > title"))# [<title>标题</title>]

# # print(soup.select("p > #link1")) # [<a class="sister" href="http://example.com/1" id="link1">链接1</a>]

# # print(soup.select("p > a:nth-of-type(2)")) # [<a class="sister" href="http://example.com/2" id="link2">链接2</a>]
# # nth-of-type 是CSS选择器

# # 查找兄弟节点（向后查找）
# # print(soup.select("#link1 ~ .sister"))
# # [<a class="sister" href="http://example.com/2" id="link2">链接2</a>,
# # <a class="sister" href="http://example.com/3" id="link3">链接3</a>]

# # print(soup.select("#link1 + .sister"))
# # [<a class="sister" href="http://example.com/2" id="link2">链接2</a>]

# # 通过属性查找
# # print(soup.select('a[href="http://example.com/1"]'))

# # # ^ 以XX开头
# # print(soup.select('a[href^="http://example.com/"]'))

# # # * 包含
# # print(soup.select('a[href*=".com/"]'))

# # # 查找包含指定属性的标签
# # print(soup.select('[name]'))

# # # 查找第一个元素
# # print(soup.select_one(".sister"))



# #!/usr/bin/env python
# # -*- coding: UTF-8 -*-
# '''Risk2S'''
# import json
# # 列表写入文件
# # 测试list
# risk_list =  [{'123':'111','456':222},{'123':'111','456':222}]
# # 将数据写入文件
# file = open('risk.json', 'w')
# for i in risk_list:
#     json_i = json.dumps(i) # doumps写入
#     file.write(json_i+'\n')
# file.close()

# # 从文件中读取数据
# risk_result = []
# with open('risk.json','r') as f:
#     # 读取数据并分割。 最后一个为空，所以去除
#     risk_new_list = f.read().split('\n')[0:-1:1] #这句话啥意思,把json格式的文件分割成一个字符串，然后返回列表的形式,以换行符为分割的标准
#     print(risk_new_list)
#     for x in risk_new_list:
#         json_x = json.loads(x) # loads读取数据
#         risk_result.append(json_x)
# f.close()
# print("原始数据是：", risk_list)
# print("结果数据是：", risk_result)