import requests
import os
import time
from bs4 import BeautifulSoup
import random
import urllib.request
 
#频繁怎么办？1.函数回调 2.延迟 3.response.close() 4.socket.setdefaulttimeout(t_default) 5换代{过}{滤}理
 
#https://www.huiyi8.com/search/%E7%BE%8E%E5%A5%B3/1.html
#https://www.huiyi8.com/search/%E7%BE%8E%E5%A5%B3/2.html
 
 # 'NoneType' object is not callable  line 33, 看样子改了网页结构，没；错误类型是说noneType对象是无法调用的
 
last_page=int(input("请输入要爬取的页数："))
n=0
headers={}
for page in range(1,last_page+1):
    print("正在爬取第{}页的图片...".format(page))
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
    headers['User-Agent'] = random.choice(user_agent_list)
    html=requests.get("https://www.huiyi8.com/search/%E7%BE%8E%E5%A5%B3/{}.html".format(page),headers=headers)
    soup=BeautifulSoup(html.text,'lxml')
    link=soup.select("li.works-box.fl.b-box div a")
 
    for i in link:
        true_html=requests.get(i['href'],headers=headers)
        time.sleep(random.randint(1,5))
        new_soup=BeautifulSoup(true_html.text,'lxml')
        new_link=new_soup.select_one('div.imgcont img')
 
        if not os.path.exists('520妹子图'):
            os.mkdir('520妹子图')
        with open('520妹子图/{}.jpg'.format(i.text),'wb')as f:
            f.write(requests.get(new_link['src'],headers=headers).content)
        print(new_link['src'])
        urllib.request.urlretrieve(new_link['src'],'1520妹子图/{}.jpg'.format(i.text))
        n+=1
        print("第{}张图片下载完成......".format(str(n)))
        time.sleep(random.randint(1,5))