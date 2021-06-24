# coding:utf-8
'''
命令行工具集 v1.0
'''
# 思路挺不错的，找到相应路劲然后打开
import os
import time
import webbrowser as web
 
def get_ipinfo():
    print('■' * 24)
    os.system('systeminfo')
    os.system('ipconfig /all')
    print('■' * 24)
    print('显示30秒')
    time.sleep(30)
 
def shutdown():
    for i in range(5):
        d = 5 - (i + 1)
        print(f"{str(d)}秒后关机")
        time.sleep(1)
    os.system('shutdown /s /t 0')
 
def open_url():
    while True:
        os.system('cls')
        print('■' * 24)
        print('1.百度搜索')
        print('2.52破解')
        print('输入任意可返回上一级')
        print('■' * 24)
        out = input("请输入要打开的网页:")
        if out == '1':
            web.open_new_tab('http://www.baidu.com')
        elif out == '2':
            web.open_new_tab('http://www.52pojie.cn')
        else:
            print('未输入指定按键，已关闭')
            break
 
def open_app():
    while True:
        os.system('cls')
        print('■' * 24)
        print('1.qq')
        print('2.wx')
        print('3.google浏览器')
        print('99.返回上一级')
        print('■' * 24)
        out = input("请输入要打开的工具:")
        if out == '1':
            app_dir = r'C:\Program Files (x86)\qq\qq.exe'  # 指定应用程序目录
            os.startfile(app_dir)
        elif out == '2':
            app_dir = r'C:\Program Files (x86)\wx\wx.exe'  # 指定应用程序目录
            os.startfile(app_dir)
        elif out == '3':
            app_dir = r'C:\Program Files (x86)\google\google.exe'  # 指定应用程序目录
            os.startfile(app_dir)
        else:
            break
 
while True:
    os.system('cls')
    print('■' * 24)
    print('1.打开快捷网址')
    print('2.快速打开应用')
    print('3.查看ip及计算机信息')
    print('4.关机')
    print('■' * 24)
    mout = input("请输入要使用的功能:")
    if mout == '1':
        open_url()
    elif mout == '2':
        open_app()
    elif mout == '3':
        get_ipinfo()
    elif mout == '4':
        shutdown()
    else:
        print('你输入的命令有误，请按照提示输入!')
        time.sleep(1.5)