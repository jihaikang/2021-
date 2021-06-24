import requests
from lxml import etree
import time
import re 
from subprocess import check_output
 #  【js逆向】Qfang网的解析与爬取
headers = { 
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Host':'shenzhen.qfang.com',
    'Connection': 'keep-alive'
    }
 
 
def c_0x25d6be(a, b):
    j = 0
    for i in range(0, len(a)):
        j += ord(a[i])
    j *= int(b)
    j += 0x1b207
    str_wzws = "WZWS_CONFIRM_PREFIX_LABEL" + str(j)
    print(str_wzws)
    return str_wzws
 
 
# 由于有302重定向，以Session保持、传递response的set-cookie
s = requests.Session()
 
# 第一次get请求：js文件中的2个变量值提取、计算得出第二次get的url参数
url = 'https://shenzhen.qfang.com/sale'
rsp_1 = s.get(url=url, headers=headers)
 
rsp_1_0x14e579 = re.findall(r"_0x14e579='(.*?)';" ,rsp_1.text)[0]
rps_1_0x351708 = re.findall(r"_0x351708='(.*?)';" ,rsp_1.text)[0]
str_wzws = c_0x25d6be(rsp_1_0x14e579, rps_1_0x351708)
 
# process模块的check_output, 以命令行运行node
js_open = check_output(['node', r'5_27\new-3.js', str_wzws], timeout=100)
url_path = js_open.decode('utf8').strip()
print(url_path)
time.sleep(1)
 
 
# 第二次get请求：
headers.update({'Referer':'https://shenzhen.qfang.com/sale'})
 
url_2 = 'https://shenzhen.qfang.com/WZWSREL3NhbGU=?wzwschallenge={0}'.format(url_path)
rsp_2 = s.get(url=url_2, headers=headers)
time.sleep(1)
 
 
# 第三次get请求：解析response获得数据
rsp_3 = s.get(url=url, headers=headers)
selector = etree.HTML(rsp_3.text)
x = selector.xpath('/html/body/div[4]/div/div[1]/div[4]/ul/li[1]/div[2]/div[1]/a/text()')
print(x) # 一次只能爬取4次