#1. 验证码的识别,获取验证码图片的文字数据
#2. 对post请求进行发送
#3. 对响应数据进行持久化存储

import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
url = 'http://www.renren.com/SysHome.do'
page_text = response.get(url = url,headers = headers).text
tree = etree.HTML(page_text)
code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
code_img_data = requests.get(url = code_img_src,headers = headers).content
with open('./code.jpg','wb') as fp:
    fp.write(code_img_data)
    
#下面需要使用打码平台提供的示例代码进行识别，云打码平台已挂
######了解视频代码使用思路即可，可自行使用其他打码平台实现操作，

#post请求发送
login_url = ' '
data = {
    
}
response = requests.post(url = login_url,headers = headers,data = data)
print(response.satus_code)

#login_page_text = response.text
#with open('renren.html','w',encoding = 'utf-8') #as fp:
    fp.write(login_page_text)