from selenium import webdriver
from  time import sleep # 调用time包中的sleep模块

bro = webdriver.Chrome() # 谷歌浏览器中的c要大写,定义一个浏览器对象，且绑定浏览器驱动
bro.get('https://baidu.com/') # 模拟浏览器发送个get请求，要以http或者https开头
# 标签定位
search_input = bro.find_element_by_name('wd') # 我定位不到搜索框 name,id,class都是常用的定位属性，我把id的属性用name方式找当然不行。
# search_input = bro.find_elements_by_xpath('/html/body/div[1]/div[2]/div[5]/div[1]/div/form/span[2]/input') 我直接使用Chrome自带的xpath与fall xpath全都失败
 # 标签的交互
search_input.send_keys('python')
# 点击搜索按钮
# btn = bro.find_elements_by_id('su') # 看来这个搜索按钮我定义错了
btn = bro.find_element_by_id('su') # find_elements_返回的是一个列表,find_element_返回的是单个元素
# btn = bro.find_elements_by_xpath('//input[@id='su'] and [@classs='btn self-btn bg s_btn']') # bro.find_elements_by_xpath与bro.find_element_by_xpath有啥区别,xpath路径用and 咋用
btn.click()
sleep(6)
bro.get('https://www.taobao.com/')
bro.back() # 后退
sleep(2)
bro.forward() # 前进
sleep(5)
bro.quit()