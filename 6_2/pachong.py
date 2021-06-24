# 需求：爬取糗事百科中糗图板块下所有的糗图图片
'''<div class="thumb">
<a href="/article/124098472" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12409/124098472/medium/HSN2WWN0TP1VUPNG.jpg" alt="糗事#124098472" class="illustration" width="100%" height="auto">
</a>
</div>'''
import re
import os
import requests

# 糗事百科的图片直接加个https:就可以了，真的哎
if __name__ == '__main__':
    # 创建一个文件夹，保存所有的图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')

    url = 'https://www.qiushibaike.com/imgrank/ '
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

    # 使用通用爬虫对url对应的一整张页面进行爬取
    page_text = requests.get(url=url, headers=headers).text
    #print(page_text)

    #使用聚焦爬虫将页面中所有的糗图进行解析提取
    ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'

    img_src_list = re.findall(ex,page_text, re.S) # 正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配。

    print(img_src_list)
    for src in img_src_list:
        #拼接出完整的图片url
        src = 'https:' + src
        # print(src)
        img_data = requests.get(url=src,headers=headers).content # 这里不加url=  headers= 就会导致无法打开而二进制文件
        #生成图片名称
        img_name = src.split('/')[-1]
        imgPath = './qiutuLibs/' + img_name
        with open(imgPath,'wb') as fp:
            fp.write(img_data)
        print(img_name, '下载成功!')