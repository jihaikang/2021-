import requests,random,time
from bs4 import BeautifulSoup
 
server_key = 'xxxx'
coolpush_key = 'xxx'
qmsg_key = 'xxx' #默认
 
def UserAgent(): #随机获取请求头
    user_agent_list = ['Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
                   'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
                   'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6',
                   'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
                   'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36']
    UserAgent={'User-Agent': random.choice(user_agent_list)}
    return UserAgent
 
 
def GetHtml(args1,args2):
    goods_list = []
    uids = ["9687682701", "5160345630"]  #什么值得买爆料人ID，可以自己添加
    try:
        for uid in uids:
            url = "https://zhiyou.smzdm.com/member/" + uid + "/baoliao/"
            response = requests.get(url, headers=UserAgent()).content
            soup = BeautifulSoup(response, 'html.parser', from_encoding='utf-8')
            html = soup.find_all(name='div', attrs={'class': 'pandect-content-title'})
            for i in html:
                goods_list.append(i.a.get_text().strip() + ' ——> ' + i.a['href'].strip())
                if goods_list[0]:
                    break;
        print(goods_list)
        select_robots(0,str(goods_list)) #0为Qmsg推送，1为酷推推送，2为server酱推送。默认为0
    except Exception as e:
        print(e)
 
 
def select_robots(i,data):
    if i == 0:
        HtmlPuch_Qmsg(data)
    elif i == 1:
        HtmlPuch_coolpush(data)
    elif i == 2:
        HtmlPuch_server(data)
    else:
        print('选择错误!')
 
 
def HtmlPuch_server(data): #server酱推送
    url_key = "https://sc.ftqq.com/" + server_key + ".send"
    push_data = {'text':"推送",'desp':data}
    html = requests.post(url_key,headers=UserAgent(),data=push_data)
 
def HtmlPuch_coolpush(data):  #酷推推送
    url_key = "https://push.xuthus.cc/send/" + coolpush_key
    push_data = {'c':data}
    html = requests.get(url=url_key,params=push_data,headers=UserAgent())
 
def HtmlPuch_Qmsg(data):  #Qmsg推送
    url_key = "https://qmsg.zendee.cn/send/" + qmsg_key
    push_data = {'msg':data}
    html = requests.get(url=url_key,params=push_data,headers=UserAgent())
