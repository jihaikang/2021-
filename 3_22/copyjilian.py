import os
import requests
from lxml import etree


if not os.path.exists('./jianli'):
    os.mkdir('./jianli')
urls = 'https://sc.chinaz.com/jianli/free.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
past = requests.get(url=urls,headers = headers).text # 获取主页面
tree = etree.HTML(past)
past1 = tree.xpath('//*[@id="container"]/div') # @属性值 = ""一定要双引号
for detail_url in past1:
    detail_url = 'https:' + detail_url.xpath('./a/@href')[0]
    detail_page_text = requests.get(url = detail_url, headers =headers).text
    tree = etree.HTML(detail_page_text)
    url = tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0] # 获取下载地址
    name = tree.xpath('//h1/text()')[0].encode('iso-8859-1').decode('utf-8')# 获取名字 xpath语句.path(''),括号内有引号
    download_contend = requests.get(url=url,headers=headers).content # 下载下载页面的内容
    file_path = 'jianli/' + name + '.rar' #建立文件夹
    with open(file_path, 'wb') as fp: # 无法写入文件，创建文件
        fp.write(download_contend)
    print(name, '下载完成')