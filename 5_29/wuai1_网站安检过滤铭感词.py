# -*- coding: UTF-8 -*-
 # 这是python2,要把python2转化为python3
import sys
 
import urllib2
 
import re
 
import uniout
 
import os
 
from datetime import datetime
 
import time
 
reload(sys)
 
sys.setdefaultencoding('utf-8')
 
url = "https://www.hao123.com/?tn=88093251_74_hao_pg"  # 要爬取的网址
 
http = "http"
 
request = urllib2.Request(url, "headers=Headers")
 
nodes = {".bmp", ".jpg", ".png", ".jpeg", ".xls", ".xlsx", ".doc", ".docx", ".wav", ".rmvb", ".mp3", ".gif", "#",
         ".mp4"}
 
filename = 'word.txt'  # txt文件和当前脚本在同一目录下，所以不用写具体路径 在文件中分行放置你要爬取的敏感词汇
pos = []
 
count = 0
 
with open(filename, 'r') as file_to_read:
    pos = file_to_read.readlines()
 
 
# 链接网址
def getResponse():
    try:
 
        response = urllib2.urlopen(request)
 
    except urllib2.HTTPError as he:
 
        print hexversion.code
 
    except urllib2.URLError as ue:
 
        print ue.reason
 
    else:
 
        return response.read().decode('utf-8')
 
 
# 获取链接
def getUrl():
    html = getResponse()
 
    patterncss = '<link href="(.*?)"'
 
    patternjs = '<script src="(.*?)"'
 
    patternimg = '<img src="(.*?)"'
 
    patternpage = '<a.*?href="(.*?)"'
 
    patternonclick = "openQuestion.*?'(.*?)'"
    # 根据正则获取标签中的url
    href = re.compile(patterncss, re.S).findall(html)
    # 爬取图片地址  一般敏感词汇用不着爬取图片 可以注释该段代码
    href += re.compile(patternimg, re.S).findall(html)
 
    href += re.compile(patternpage, re.S).findall(html)
 
    href += re.compile(patternjs, re.S).findall(html)
 
    href += re.compile(patternonclick, re.S).findall(html)
    hrefs = []
 
    for h in href:  # 根据规则去除多余连接
        for n in nodes:
            if n.upper() not in h.upper():
                hrefs.append(h)
                break
 
    hrefs = list(set(hrefs))  # 去重
    return hrefs
 
 
def reasonCode():
    itemurl = getUrl()
 
    for item1 in itemurl:
 
        if http in item1:
            getUrlMsg(item1)
 
 
# 爬虫内容对比关键字
def getUrlMsg(aa):
    global count
    ss = []
    try:
        response = urllib2.urlopen(urllib2.Request(aa, "headers=Headers"))
        bb = response.read()
        for po in pos:
            postr = ''.join(po.split())
            if postr in bb and postr is not '':
                ss.append(postr)
        if len(ss) > 0:
            print '敏感网址', aa, str(ss).decode('string_escape')
            greatMirk('敏感网址' + str(count), bb)
        else:
            print '该网址合格:', aa
        count += 1
    except Exception as e:
        count += 1
        print e, ' ', aa
        pass
 
 
# 创建文件下载html
def greatMirk(name, msg):
    filename = 'd:/html/' + name.decode('utf-8') + '.html'
 
    if os.path.exists(filename):
        with open(filename, 'wb') as ff:
            ff.write(msg)
    else:
        with open(filename, 'wb') as ff:
            ff.write(msg)
 
 
starTime = datetime.now()  # 获得当前时间
reasonCode()
endTime = datetime.now()  # 获取当前时间
durn = (endTime - starTime).seconds  # 两个时间差，并以秒显示出来
print ('在', durn, '秒内爬取了', count, '个网址')