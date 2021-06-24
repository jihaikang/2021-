# 需要添加的模块
from bs4 import BeautifulSoup
import re
import urllib.request
 
 
def main():
    baseurl = "https://movie.douban.com/top250?start="  # 爬取豆瓣
    top250 = getData(baseurl)
    saveData(top250)
 
 
movie_Name = re.compile(r'<span class="title">(.*?)</span>')  # 电影名称
movie_Link = re.compile(r'<a href="(.*?)">')  # 电影链接
movie_Img = re.compile(r'<img.*src="(.*?)"', re.S)  # 图片链接
movie_Rating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')  # 评分
movie_Judge = re.compile(r'<span>(\d*)人评价</span>')  # 评价人数
movie_survey = re.compile(r'<span class="inq">(.*?)</span>')  # 电影概况
movie_info = re.compile(r'<p class="">(.*?)</p>', re.S)  # 相关信息
 
 
# 1.爬取网页
def add(baseurl):
    head = {
        "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/71.0.3578.98 Safari/537.36"
    }  # 模拟浏览器
    request = urllib.request.Request(url=baseurl, headers=head)
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    return html
 
 
# 2.获取数据
def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        gain = add(url)
        soup = BeautifulSoup(gain, "html.parser") # 报错，不知是改了网页结构还是啥
        for item in soup.find_all("div", class_="item"):  # 截取网页
            item = str(item)
            name = re.findall(movie_Name, item)[0]  # 电影名,使用正则来匹配内容(逐一解析)
            link = re.findall(movie_Link, item)[0]  # 电影链接
            img = re.findall(movie_Img, item)[0]  # 图片链接
            rating = re.findall(movie_Rating, item)[0]  # 评分
            judge_num = re.findall(movie_Judge, item)[0]  # 评价数量
            survey = re.findall(movie_survey, item)  # 概况
            if len(survey) != 0:
                survey = survey[0].replace("。", "")  # 去掉句号
            else:
                survey = ""  # 留空
            info = re.findall(movie_info, item)[0]  # 相关信息
            info = re.sub("/", " ", info)  # 替换/
            info = re.sub(r" + |\xa0|\n|<br >", "", info)  # 去掉其他
            data = [name, link, img, rating, judge_num, survey, info]  # 保存数据
            datalist.append(data)  # 追加到列表
    return datalist
 
 
# 3. 保存数据
def saveData(top250):
    f = open("豆瓣Top250.txt", "w", encoding='utf-8')
    for i in range(0, 249):
        print("已存储第%d条影片信息" % (i+1))
        data = top250[i]
        movie = str(data)
        f.write(movie + "\n")  # 写入内容
    f.close()
 
 
if __name__ == '__main__':
    main()
    print("人生苦短,我用Python")