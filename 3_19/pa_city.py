# 需求：解析出所有城市名称  https://www.aqistudy.cn/historydata/
import requests
from lxml import etree

if __name__ == '__main__':
    '''headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)

    #数据解析
    hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    all_city_names = []
    #解析热门城市名字
    for li in hot_li_list:
        hot_city_names = li.xpath('./a/text()')[0]
        all_city_names.append(hot_city_names)

    #解析全部城市名字：
    city_names_list = tree.xpath('.//div[@class="bottom"]/ul/div[2]/li')
    for li in city_names_list:
        city_name = li.xpath('./a/text()')[0]
        all_city_names.append(city_name)

    print(all_city_names,len(all_city_names))'''

    # 第二种方法，一起解析

    headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    # 数据解析  解析到热门城市和全部城市对应的a标签
    # 热门城市标签层级div/ul/li/a
    # 全部城市标签层级div/ul/div[2]/li/a
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a ')
    all_city_names = []
    for a in a_list:
        a_name = a.xpath('./text()')[0]
        all_city_names.append(a_name)
        # fp = open('city.txt','w',encoding = 'utf-8')
        # fp.writelines(all_city_names + '\n\n') 
    # a_str = str(all_city_names).replace('{', '').replace('}', '').replace("'", '').replace(':', ',') + '\b'
    for i in range(len(all_city_names)):
        a_str = str(all_city_names[i]).replace('{', '').replace('}', '').replace("'", '').replace(':', ',') + '\b'
        # print(i)
        # print(type(a_str))
        with open('cit.txt','w',encoding='utf-8') as fp:
            fp.write( a_str+'\n')   # 数据持久化写入列表为列表的最后一项：方法write
    # print(all_city_names, len(all_city_names))