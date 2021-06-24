from selenium import webdriver
from  time import sleep # 调用time包中的sleep模块

bro = webdriver.Chrome() # 谷歌浏览器中的c要大写
bro.get('https://baidu.com/') # 模拟浏览器发送个get请求，要以http或者https开头
 # 标签定位
# search_input = bro.find_elements_by_class_name('s_kw_wrap') # 我定位不到搜索框
 # 标签的交互
# search_input.send_keys('python')
# 点击搜索按钮
# btn = bro.find_elements_by_class_name('btn self-btn bg s_btn')
# btn.click()
sleep(2)
bro.get('https://www.taobao.com/')
bro.back() # 后退
sleep(2)
bro.forward() # 前进
sleep(5)





bro.quit() # 要及时结束，释放资源,不加括号的话浏览器不会关闭，控制台会结束这段代码