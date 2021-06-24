# 看来有问题，没有推送到我手机上


import requests
import json
import datetime
 
global contents
contents = ''
 
def sign(): 
    #金山词霸每日一句
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    r = json.loads(r.text)
    content = r["content"]
    note = r["note"]
    daily_sentence = content + "\n" + note
 
    # 获取日期和倒计时    
    a = datetime.datetime.now()  # 实施时间
    y = str(a.year)
    m = str(a.month)
    d = str(a.day)  # 转换为字符串，便于打印
    time = y + '年' + m + '月' + d + '日' + '\n'
    b = datetime.datetime(2021, 6, 12)  # 自己设置的研究生考试时间
    count_down = (b - a).days  # 考研倒计时
    count_down = '考研倒计时{}天，加油哦！'.format(count_down) 
 
    # qq推送
    qqtalk = 'https://qmsg.zendee.cn/send/9b55030bd2e4a2cdd54d066bc2d02e49?msg=' +count_down+'\n' + daily_sentence + '&qq=[2993431608]'
    requests.get(qqtalk)
 
def main():
    sign()
 
def main_handler(event, context):
    return main()
 
if __name__ == '__main__':
    main()