# a = '//pic.qiushibaike.com/system/pictures/12438/124387507/medium/C11OK8O3YW0DYSVM.jpg'
# print(a.split('/')[-1]) # split是以什么作为分隔符，然后得到该分割后匹配的字母
# print(a)

# format用法 
#1可以用传统的%
# print(format('%d' % 12))
# print('%d%d' %(1,2))
# #2{}顺序（数值）匹配
# print('a{0}pl{1}'.format('p','e'))
# # print(format.('a{0}pl',e)) # 不能用format函数包裹的方式

# #2{}也可以通过键值来匹配：
# print('a{qp}pl{pe}'.format(qp='p',pe='e')) #键不能是数字


# for pageNum in range(11):
#     print(pageNum)


from bs4 import BeautifulSoup
from bs4.builder import XML

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html,'lxml')
b = BeautifulSoup(html,'lxml')
print("-"*100)
print(soup.prettify()) # 美化html what
print("+"*100)
print(soup.title)
print("+"*100)
print(soup.title.name)
print("+"*100)
print(soup.title.string)
print("+"*100)
print(soup.title.parent.name)
print("+"*100)
print(soup.p)
print("+"*100)
print(soup.p["class"])
print("+"*100)
print(soup.a)
print("+"*100)
print(soup.find_all('a'))
print("+"*100)
print(soup.find(id='link3'))
print("-"*100)