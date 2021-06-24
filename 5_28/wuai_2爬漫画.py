import requests
import re #正则匹配
from bs4 import BeautifulSoup #解析网页内容
import urllib.parse #将内容转换为urlencode格式

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }

#下载网页用于分析内容
def down_one_page(url):
    respond = requests.get(url,headers=headers)
    if(respond.status_code == 200):
        return respond.content.decode()
    return 'err'

#将实际内容下载为文件保存到本地
def download(name,url):
    file = requests.get(url,headers=headers)
    with open(name,'wb') as f:
        f.write(file.content)

begin_url = 'https://www.zymk.cn/66/'
html = down_one_page(begin_url)
soup = BeautifulSoup(html,'lxml')
results = soup.find_all(attrs = {'class':'chapter-list clearfix'})
datas = re.findall('href="(.*?)"',str(results),re.S) #获取章节列表
datas.reverse() #列表倒序

print('漫画神精榜下载')
print('请输入需要下载的章节1-' + str(len(datas)))
begin = int(input('开始章节：'))
end = int(input('结束章节：'))

#审查元素获得的图片地址https://mhpic.xiaomingtaiji.net/comic/S%2F%E7%A5%9E%E7%B2%BE%E6%A6%9C%2F1%E8%AF%9DGQ%2F1.jpg-zymk.middle.webp
#url..为自己发现的规律所拆分的分段网址,S%2F%E7%A5%9E%E7%B2%BE%E6%A6%9C%2F1%E8%AF%9DGQ%2F1 为中文urlencode编码和页码

url1 = 'https://mhpic.xiaomingtaiji.net/comic/S%2F%E7%A5%9E%E7%B2%BE%E6%A6%9C%2F'
url3 = 'GQ%2F'
#url4 = '.jpg-zymk.middle.webp'  #网页原图片为webp格式，保存下来不方便查看，查了资料说可以直接保存为.jpg
url4 = '.jpg-zymk.middle.jpg'

#循环下载章节
for i in range(begin-1,end):
    url = begin_url + str(datas[i])
    html = down_one_page(url)
    max_page = re.findall('end_var:(.*?),comic_',html,re.S)
    name = re.findall('chapter_name:"(.*?)"',html,re.S)
    name = name[0]
    url2 = urllib.parse.quote(name)
#循环下载章节下的分页
    for num in range(1,int(max_page[0])+1):
        url = url1+url2+url3+str(num)+url4
        download(name+' '+str(num)+'.jpg',url)
#输出进度
    print('已完成 第'+ name)

i = None
while(i == None):
    i = input('按Enter键退出')