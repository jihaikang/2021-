from selenium import webdriver
from lxml import etree
from time import sleep
# 实例化一个浏览器对象（传入浏览器的驱动程序）
bro = webdriver.Chrome()
# 让浏览器发起一个指定的url对应请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')     

# 获取浏览器当前页面的页面源码数据
page_text = bro.page_source
print(page_text)
bro.quit()

# import re
# string = 'aliyun'
# res = re.search("a",string).span() # 是返回下标
# print(res) 
