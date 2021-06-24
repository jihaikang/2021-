import requests
from lxml import etree
import os 


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

url = 'https://www.aqistudy.cn/historydata/'
respons = requests.get(url = url,headers= headers).text
tree = etree.HTML(respons)
path_text = tree.xpath('//div[@style = "padding:10px 10px 0 10px"]/ul/li')
main_city = [] 
fp = open('city1.txt','w',encoding = 'utf-8')
for i in path_text:
   city_name =i.xpath('./a/text()')[0]
   main_city.append(city_name)
   fp.writelines(main_city )# 换行符是\n不是/n,用加号连接
print(main_city,len(main_city))