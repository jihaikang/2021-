# import os
# import re
# import random
# import requests
# 同步代码
# from datetime import datetime

# from lxml import etree

# class Sync:
#     headers = {
#         'User-Agent':
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
#     }
#     if not os.path.exists('./videos'): # 创建文件夹
#         os.mkdir('./videos')
#     download_folder = "./videos"

#     def run(self):
#         url = 'https://www.pearvideo.com/category_5'

#         resp = requests.get(url, headers=self.headers)
#         if resp.status_code == 200:
#             tree = etree.HTML(resp.text)
#             lis = tree.xpath('//ul[@id="categoryList"]/li')
#         else:
#             raise requests.RequestException

#         for li in lis:
#             filename, download_url = self.parse_video_url(li)
#             print(f"==> 开始下载 {filename}")
#             self.download(filename, download_url)

#     def parse_video_url(self, li) -> tuple:
#         title = li.xpath('./div/a/div[2]/text()')[0].strip('“”！？').replace("| ", "").replace(" | ", "")

#         page = str(li.xpath('./div/a/@href')[0]).split('_')[1]

#         ajax_url = 'https://www.pearvideo.com/videoStatus.jsp?'
#         params = {'contId': page, 'mrd': random.random()}
#         headers = self.headers.copy()
#         headers.update({'Referer': 'https://www.pearvideo.com/video_' + page})

#         resp = requests.get(ajax_url, headers=headers, params=params)

#         ajax_text = resp.json()
#         download_url = ajax_text["videoInfo"]['videos']["srcUrl"]
#         download_url = re.sub(r"\d{13}", f"cont-{page}", download_url)

#         return title + ".mp4", download_url

#     def download(self, filename: str, url: str):
#         resp = requests.get(url, headers=self.headers)
#         if resp.status_code == 200:
#             content = resp.content

#             with open(os.path.join(self.download_folder, filename), "wb") as fb:
#                 fb.write(content)

#             print(f"已下载：{filename}")
#             print("-" * 60)
#         else:
#             raise requests.RequestException

# if __name__ == '__main__':
#     start = datetime.now()

#     s = Sync()
#     s.run()

#     end = datetime.now()

#     print((end - start).total_seconds(), "秒") # 35.208142 秒

# 异步会在当前进务阻塞时挂起当前任务去执行另一个任务，而同步则只能在阻塞时一直等待，所有任务排队执行。

# 当前下载的文件较少，阻塞的时间也较短，异步效率大概是同步的 2 ~ 3 倍，如果下载的文件更多，阻塞时长增加，异步的下载效率还能更高。



# 异步代码

import os
import re
import random
import asyncio
import aiofiles
import aiohttp

from datetime import datetime
from lxml import etree

class Spider:
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    
    download_folder = "./videos"

    urls = []

    async def main(self):
        await self._get_video_urls()

        downloader = [asyncio.create_task(self._download_video(filename, url)) for filename, url in self.urls]
        await asyncio.gather(*downloader)

    async def _get_video_urls(self):
        url = 'https://www.pearvideo.com/category_5'

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    text = await response.text()
                    tree = etree.HTML(text)
                    lis = tree.xpath('//ul[@id="categoryList"]/li')
                else:
                    raise aiohttp.ClientResponseError

        spider = [self._parse_video_url(li) for li in lis]
        await asyncio.wait(spider)

    async def _parse_video_url(self, li):
        title = li.xpath('./div/a/div[2]/text()')[0].strip('“”！？').replace("| ", "").replace(" | ", "")

        page = str(li.xpath('./div/a/@href')[0]).split('_')[1]

        ajax_url = 'https://www.pearvideo.com/videoStatus.jsp?'
        params = {'contId': page, 'mrd': random.random()}
        headers = self.headers.copy()
        headers.update({'Referer': 'https://www.pearvideo.com/video_' + page})

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(ajax_url, params=params) as response: #显示这里错了
                ajax_text = await response.json()
                download_url = ajax_text["videoInfo"]['videos']["srcUrl"]
                download_url = re.sub(r"\d{13}", f"cont-{page}", download_url)
                self.urls.append((title + ".mp4", download_url))

    async def _download_video(self, filename: str, url: str):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            print(f"开始下载 => {filename}")
            async with session.get(url, headers=self.headers) as response:
                content = await response.read()

        async with aiofiles.open(os.path.join(self.download_folder, filename), "wb") as fb:
            await fb.write(content)

        print(f"已下载 => {filename}.mp4")

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())

if __name__ == '__main__':
    start = datetime.now()

    s = Spider()
    s.run()

    end = datetime.now()

    print("=" * 40)
    print((end - start).total_seconds(), "秒")