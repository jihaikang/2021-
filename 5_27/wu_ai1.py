import requests
from bs4 import BeautifulSoup
 
 
def get_Url(url):
    str_list = []
    content = requests.get(url).content # 获取网页源码
    soup = BeautifulSoup(content, 'lxml')
    find = soup.find('span', attrs={'class': 'current'})
    sum = int(find.text.split('/')[1])
    for i in range(sum):
        if i == 0:
            str_list.append('https://www.mycodes.net/166/')
            continue
        str_list.append('https://www.mycodes.net/166/' + str(i + 1) + '.htm')
    return str_list
 
 
def get_document(url):
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    find_all = soup.find_all('a', attrs={'style': 'color:#006BCD;font-size:14px;'})
    a = ''
    for value in find_all:
        if a.__eq__(str(value['href'])):
            continue
        a = value['href']
        document = BeautifulSoup(requests.get(value['href']).content, 'lxml')
        text = document.find('td', attrs={'class': 'a0'}).text
        print(text+":")
        td_s = document.find_all('td', attrs={'class': 'b4'})
        for td in td_s:
            find = td.find('a')
            if find is not None:
                href_ = 'https://www.mycodes.net' + find['href']
                down = requests.get(href_)
                with open('d:/HTML_sourse_ma/'+text+".zip", "wb") as code:
                    code.write(down.content)
                break
 
 
 
if __name__ == '__main__':
    url_list = get_Url('https://www.mycodes.net/166/')
    for url in url_list:
        get_document(url) # 这个爬取的速度好慢啊，估计能不能用多线程实现下