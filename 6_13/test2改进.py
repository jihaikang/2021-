# from tkinter import *

# win = Tk()
# # 不加注释你们也看得董
# def update(ls):
#     print(ls)
#     txt.delete("1.0", END)
#     txt.insert(END, ','.join(map(str, ls))+'\n')
#     cancel_id = txt.after(1000, update, ls)
#     if len(ls)>5:
#         ls.pop()
#     else:
#         txt.after_cancel(cancel_id)
    
# txt = Text(win)
# txt.insert(END, "Hello\n")
# txt.pack()

# ls = list(range(9))
# win.after(1000, update, ls)

# win.mainloop()


import urllib.request
import requests
#  响应好慢
url = 'http://httpbin.org/get'
# html = requests.get(url).read()  # requests请求返回页面源码都不会了
proxy_support = urllib.request.ProxyHandler({'http':'49.232.118.212:3128'})  # 构建网络代理

opener = urllib.request.build_opener(proxy_support)  # 这个也有研究的价值
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)