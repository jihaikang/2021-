#需求：爬取58二手房中的房源信息
#作者提醒：此处代码与视频课中有差别，原因是视频课拍摄时的网页源码和作者实际学习时网页源码有变化，作者代码于2021/02/26运行正常。
import time
import requests
from lxml import etree
if __name__ == '__main__': 
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    #爬取页面源码数据
    url = 'https://bj.58.com/ershoufang/'
    page_text = requests.get(url = url,headers = headers).text
    
    #数据解析
    tree = etree.HTML(page_text)
    #存储的是标签对象
    div_list = tree.xpath('//section[@class="list"]/div')
    fp = open('50.txt','w',encoding = 'utf-8')
    for div in div_list:
        #页面数据的局部解析
        title = div.xpath('./a/div[2]//h3/text()')[0] #<class 'lxml.etree._ElementUnicodeResult'>可以写入txt文件
        print(title)
        print('*'*100)
        print(type(title))
        # fp.writelines(title + '\n\n')
print('---------------Over!------------------')