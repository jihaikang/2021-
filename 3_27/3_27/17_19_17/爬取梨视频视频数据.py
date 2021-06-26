# 需求：爬取梨视频视频数据
import requests
import os
from multiprocessing.dummy import Pool #多线程池
from lxml import etree  ##xpath解析 # 我还是很难获取到对的xpath2021/3/26/19:47
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
# 原则：线程池处理的是阻塞且耗时的操作

if __name__ == '__main__':
    # 生成一个存放视频的文件夹
    if not os.path.exists('./video'):
        os.mkdir('./video')
        # 对下述url发起请求解析出视频详情页的url和视频的名称
    url = 'https://www.pearvideo.com/category_5'
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
urls = []  # 存储所有视频的链接和文字
for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    # print(detail_url,name)

    # 对详情页的url发起请求
    detail_page_text = requests.get(url=detail_url, headers=headers).text
    # 从详情页中解析出视频的地址
    #### 视频的方法在2021/02/27 不可使用，梨视频又更改了页面源码，mp4是动态加载出来的，mp4文件经ajax请求得到，需要抓包ajax
    #### 参考 https://www.cnblogs.com/qianhu/p/14027192.html的操作
    detail_tree = etree.HTML(detail_page_text)
    name = detail_tree.xpath('//*[@id="detailsbd"]/div[1]/div[2]/div/div[1]/h1/text()')[0]
    str_ = str(li.xpath('./div/a/@href')[0]).split('_')[1]
    ajax_url = 'https://www.pearvideo.com/videoStatus.jsp?'
    params = {
        'contId': str_,
        'mrd': str(random.random())
    }
    ajax_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Referer': 'https://www.pearvideo.com/video_' + str_
    }
    dic_obj = requests.get(url=ajax_url, params=params, headers=ajax_headers).json()
    video_url = dic_obj["videoInfo"]['videos']["srcUrl"]

    video_true_url = ''
    s_list = str(video_url).split('/')
    for i in range(0, len(s_list)):
        if i < len(s_list) - 1:
            video_true_url += s_list[i] + '/'
        else:
            ss_list = s_list[i].split('-')
            for j in range(0, len(ss_list)):
                if j == 0:
                    video_true_url += 'cont-' + str_ + '-'
                elif j == len(ss_list) - 1:
                    video_true_url += ss_list[j]
                else:
                    video_true_url += ss_list[j] + '-'
    dic = {
        'name': name,
        'url': video_true_url
    }
    urls.append(dic)


def get_video_data(dic):
    urll = dic['url']
    data = requests.get(url=urll, headers=headers).content
    path = './video/' + dic['name'] + '.mp4'
    print(dic['name'], '正在下载.......')
    # 持久化存储操作
    with open(path, 'wb') as fp:
        fp.write(data)
        print(dic['name']+ '.mp4', '下载成功！')


# 使用线程池对视频数据进行请求（较为耗时的阻塞操作）
pool = Pool(4)
pool.map(get_video_data, urls) # urls只有4个

pool.close()
pool.join()