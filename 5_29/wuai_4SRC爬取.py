import requests
import json
from lxml import etree
#  list index out of range  line 28,
class Src(object): 
    def __init__(self,page):
        self.url = "https://www.butian.net/Reward/pub"
        self.headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                'Cookie': ''
        }
        self.page=page
        self.data={
                's': '1',
                'p':self.page, 
                'token':'' 
        }

    def get_cid(self):
        r = requests.post(url=self.url,headers=self.headers,data=self.data).content.decode()
        s=json.loads(r)
        l=s['data']['list']
        for i in l:
            for k,v in i.items():
                if 'company_id' == k :
                    m=requests.get(url='https://www.butian.net/Loo/submit?cid='+v,headers=self.headers).content
                    n=etree.HTML(m)
                    value = n.xpath('//*[@id="tabs"]/form/div[1]/ul/li[3]/input/@value')[0]
                    print(value)
if __name__ == "__main__":
    for page in range(1,30):
        src=Src(page)
        src.get_cid()