import requests
import re
import os


url = 'https://www.qiushibaike.com/imgrank/page/%d/' # 用python的%d代表数字 又忘记加/左斜杠
for pageNum in range(1,11): # 大的for循环,遍历到最后页面执行退出,之后的语句都在这个循环下
    new_url = format(url % pageNum) # 可以这样格式化字符串啊
# print(new_url)
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

    page_text = requests.get(url=new_url,headers=headers).text
    ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
    img_list = re.findall(ex, page_text, re.S) # re.S可处理匹配到换行的字符串

    if not os.path.exists('./qiushi'):
        os.mkdir('./qiushi')
    for img in img_list:
        img_url = 'https:' + img
        print(img_url)
        img_name = img.split('/')[-1]
        img_data = requests.get(url=img_url,headers=headers).content
        img_path = './qiushi/' + img_name # +号就可以变成这种形式：./qiushi/img_name 可以自己加个/ 我傻了 没加/导致无法写入图片
        with open(img_path,'ab+') as f: # 这里为啥写不进去文件啊  img_path = './qiushi' + img_name  我这里少加了个/
            f.write(img_data)
        print(img_name,'下载成功')

