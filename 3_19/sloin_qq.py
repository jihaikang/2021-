from selenium import webdriver
from time import sleep

bro = webdriver.Chrome()
bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')

a_tag = bro.find_element_by_id('switcher_plogin') # 查看源码，不对劲啊，我这没找到对应id，可开发者模式就很容易找到了
a_tag.click()

userName_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')
sleep(1)
# 输入账号密码
userName_tag.send_keys('2993431608')
password_tag.send_keys('1024jihaikang')
sleep(1)
btn = bro.find_element_by_id('login_button')
btn.click()

sleep(3)