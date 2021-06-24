import requests

class HtmlDownloader:
    
    def download(self,url):
        # 判断url是否为空
        if url is None:
            return None
        print("开始下载数据，网址{0}".format(url))
        response = requests.get(url) 
        response1 = requests.post(url='',params='',) # post或者get请求只要发出了，就一定会执行
        # 如果请求成功，则返回网页数据，否则返回None
        if response.status_code == 200:
            print("下载数据成功")
            # 指定使用utf-8编码
            response.encoding = 'utf-8'
            return response.text
        return None


if __name__ == "__main__":
    url = 'http://www.bing.com/'
    d = HtmlDownloader()
    bing_html = d.download(url)
    print(bing_html)
    