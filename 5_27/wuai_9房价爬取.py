import requests
from bs4 import BeautifulSoup
import csv
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
lss=[]
for i in range(23):
    url='https://ty.anjuke.com/sale/b253-p{}/?from=esf_list'.format(i)
    html = requests.get(url, headers=headers).text
    soup=BeautifulSoup(html,'lxml')
    divs=soup.find_all('div',class_='property-content-detail')
    list1=[]
    for div in divs:
        m=div.find_all('p',class_='property-content-info-text')[1].text.replace('\n',' ').strip()
        xiaoqu=div.find('p', class_='property-content-info-comm-name').text
        weizhi=div.find('p', class_='property-content-info-comm-address').text
        ls=[]
        ls.append(m)
        ls.append(xiaoqu)
        ls.append(weizhi)
        list1.append(ls)
    jiages=soup.find_all('div',class_='property-price')
    list2=[]
    for jiage in jiages:
        zongjia=jiage.find('p',class_='property-price-total').text
        danjia=jiage.find('p', class_='property-price-average').text
        ls2=[]
        ls2.append(danjia)
        ls2.append(zongjia)
        list2.append(ls2)
    list=[]
    for i in range(len(list1)):
        list3=list1[i]+list2[i]
        list.append(list3)
        lss.append(list3)
        '''
        for i in list:
            print(i)
        '''
print(lss)
with open('G:/pythondemo/安居客/房价.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in lss:
        writer.writerow(row)