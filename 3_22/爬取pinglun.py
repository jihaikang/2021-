import requests
from lxml import etree

headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
url = 'https://vacations.ctrip.com/travel/detail/p22125398/?city=376'  # 网页页面复杂，很难爬取
page_text = requests.get(url=url,headers = headers).text
tree = etree.HTML(page_text)
cont = tree.xpath(//div[@class='ct-layout']/div/div/div/div[3]/div/div[2]/p/text()) # invalid syntax
print(cont)