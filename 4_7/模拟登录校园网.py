import json
from selenium import webdriver
from time import sleep

with open('账号密码.txt', 'r') as f: # 把json数据打开
        for line in f.readlines(): # 提取多行json数据
            json_data = json.loads(line) #一行一行编码成字典
# print(type(json_data))查看类型
def deng_lu():
    bro = webdriver.Chrome() # 谷歌浏览器中的c要大写,定义一个浏览器对象，且绑定浏览器驱动
    bro.get('http://172.30.1.160:8080/Self/login/?302=LI') # 模拟浏览器发送个get请求，要以http或者https开头

    try:
        for item in json_data:
            # 标签定位
            sleep(10)
            search_input = bro.find_element_by_id('account') 
            search_input.send_keys(item)
            search_inputs = bro.find_element_by_id('password')
            search_inputs.send_keys (json_data[item])
            sleep(10)
            # 点击搜索按钮
            btn = bro.find_element_by_name('submit') # 连续输入4次密码则会出现验证码
            btn.click()
            sleep(10)
            if bro.find_element_by_xpath('//*[@id="errorTip"]/div/text()')=='账号或密码出现错误！': # 这句话是不管找没找到他都执行,不对吧，因该是只有在element插件下才会存在这样的问题
                #把输错的账号密码写入文件
                fp = open('wrong_account.txt','a',encoding='utf-8') 
                fp.write(item)
                continue
            # 我怎么知道他返回成功或者失败呢，一般会返回什么
            else:
            # 注销登录
                search_input_zx = bro.find_element_by_class_name('btn')
                search_input_zx.click() # 之前这个直接把btn.click()复制下来弄了半小时哎，不看解析器的错误提是 
                sleep(10)
                fe = open('right_account.txt','a',encoding='utf-8')
                fe.write(item +'\n') 
                fe.write(json_data[item])
    # except:		#except从子类到父类，最后可以增加BaseException
    #     print('程序错误，慢慢找吧')
    except ValueError:
        print('只能输入数字串')
deng_lu()