# 爬取站长素材中免费的简历模板  https://sc.chinaz.com/jianli/free.html
# 代码参考：https://blog.csdn.net/nanke_nk/article/details/108966854
import os
import requests
from lxml import etree

if __name__ == '__main__':
    if not os.path.exists('./jianli'):
        os.mkdir('./jianli')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://sc.chinaz.com/jianli/free_%d.html'
    page = int(input('您一共想要爬取多少页：'))
    for pageNum in range(1, page):
        if pageNum == 1:
            new_url = 'https://sc.chinaz.com/jianli/free.html'
        else:
            new_url = format(url%pageNum)
        page_text = requests.get(url = new_url, headers = headers).text
        tree = etree.HTML(page_text)
        url_div_list = tree.xpath('//*[@id="container"]/div')
        for detail_url in url_div_list:
            detail_url = 'https:' + detail_url.xpath('./a/@href')[0]

            detail_page_text = requests.get(url = detail_url, headers =headers).text
            tree = etree.HTML(detail_page_text)
            name = tree.xpath('//h1/text()')[0].encode('iso-8859-1').decode('utf-8')
            download_url = tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
            file_path = 'jianli/' + name + '.rar'
            download_content = requests.get(url = download_url, headers = headers).content
            with open(file_path, 'wb') as fp:
                fp.write(download_content)
            print(name, '下载完成')
print('-------------------------------OVER!---------------------------------------')