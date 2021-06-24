import requests
from lxml import etree

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
url = 'https://book.douban.com/top250'
data = requests.get(url=url, headers = headers).content
tree = etree.HTML(data)
vv = tree.xpath('//*[@id="content"]/div/div[1]/div/table[8]/tbody/tr/td[2]/p[1]')# xpath提取的文件是什么
# print(url_div_list)
for i in vv:
    print(i)
# print(vv) # 如何把列表写入文件,把列表一个一个打印出来
