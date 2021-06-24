from selenium import webdriver
from lxml import etree
from time import sleep
# 实例化一个浏览器对象（传入浏览器的驱动程序）
option = webdriver.ChromeOptions()
# 防止打印一些无用的日志
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging']) #加入这5，7，8行就可以不用打印出（USB: usb_device_handle_win.cc:1056 Failed to read descriptor from node conne）
bro = webdriver.Chrome(chrome_options=option)
# bro = webdriver.Chrome()
# 让浏览器发起一个指定的url对应请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')    #get方法不需要heraeds，模拟浏览器

# 获取浏览器当前页面的页面源码数据
page_text = bro.page_source

# 解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    # name_url = li.xpath('./dl/a/@herf')[0] # 获取失败
    print(name)
sleep(5)
bro.quit()