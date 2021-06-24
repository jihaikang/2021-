from selenium import webdriver
from time import sleep
# 导入动作链对应的类
from selenium.webdriver import ActionChains

bro = webdriver.Chrome() #把selenium放在chorme目录和python目录下

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-example-droppable')

# 如果定位的标签是存在与iframe标签之中的，直接通过find方式会报错，则必须通过另外的操作来进行标签定位
bro.switch_to.frame('iframeResult')     #切换浏览器标签定位的作用域
div = bro.find_element_by_id('draggable')

# 动作链
action = ActionChains(bro)      #实例化动作链对象
# 点击并且长按指定的标签
action.click_and_hold(div)

for i in range(5):
    #perform 表示立即执行动作链操作
    #move_by_offset(x,y)   x表示水平方向，y表示竖直方向
    action.move_by_offset(11, 0).perform()
    sleep(0.3)

# 释放动作链
action.release()

bro.quit()