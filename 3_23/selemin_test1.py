from selenium import webdriver
from time import sleep
bro = webdriver.Chrome()
bro.get('https://www.taobao.com/')
# 标签定位
search_input = bro.find_element_by_id('q') #.find_element_by_id
# 标签的交互
search_input.send_keys('iphone') #.send_keys标签交互
# 执行一组js程序   相当于F12--Console执行js代码
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)') # .exexute_script()执行js程序
sleep(2)
# 点击搜索按钮
btn = bro.find_element_by_css_selector('.btn-search')
btn.click() # 点击，target在前

bro.get('https://baidu.com/')

sleep(2)
# 回退
bro.back()
sleep(2)
# 前进
bro.forward()

sleep(5)
bro.quit()