from selenium import webdriver
from  time import sleep # 调用time包中的sleep模块

account_xy = '1920014049'
password_xy = '181822'
bro = webdriver.Chrome() # 谷歌浏览器中的c要大写,定义一个浏览器对象，且绑定浏览器驱动
bro.get('http://172.30.1.160:8080/Self/login/?302=LI') # 模拟浏览器发送个get请求，要以http或者https开头
# 标签定位
search_input = bro.find_element_by_id('account') 
search_input.send_keys(account_xy)
search_inputs = bro.find_element_by_id('password')
search_inputs.send_keys(password_xy)
# 点击搜索按钮
btn = bro.find_element_by_name('submit') # 连续输入4次密码则会出现验证码
btn.click()
sleep(10)
# 注销登录
search_input_zx = bro.find_element_by_class_name('btn')
search_input_zx.click() # 之前这个直接把btn.click()复制下来弄了半小时哎，不看解析器的错误提是 
sleep(4)
account_xy1 = '1920014027'
password_xy1= '203029'
# 标签定位
search_input = bro.find_element_by_id('account') 
search_input.send_keys(account_xy1)
search_inputs = bro.find_element_by_id('password')
search_inputs.send_keys(password_xy1)
# 点击搜索按钮
btn = bro.find_element_by_name('submit') # 连续输入4次密码则会出现验证码
btn.click()
# 大致写个for循环
for data in data_ap:
    try:
    # 标签定位
    search_input = bro.find_element_by_id('account') 
    search_input.send_keys(data.account)
    search_inputs = bro.find_element_by_id('password')
    search_inputs.send_keys(data.password)
    # 点击搜索按钮
    btn = bro.find_element_by_name('submit') # 连续输入4次密码则会出现验证码
    btn.click()
    sleep(10)
    # 注销登录
    search_input_zx = bro.find_element_by_class_name('btn')
    search_input_zx.click() # 之前这个直接把btn.click()复制下来弄了半小时哎，不看解析器的错误提是 
    sleep(4)
    Exception：
    print('账号密码不适合')