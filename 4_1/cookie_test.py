# 获取Cookie
import http.cookiejar
import urllib.request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)# 创建一个头
opener = urllib.request.build_opener(handler)
url =  'http://www.biyin.com' # 连接必应的cookie失败
response = opener.open(url)
for item in cookie:
    print(item.name + '=' + item.value)