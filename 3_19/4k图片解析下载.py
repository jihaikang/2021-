import requests
from lxml import etree
import os

# 下载图片最重要的就是解析出每张图片的地址，方便request.().content下载
# 然后就是解析出每张图片的名字
# with op('./pclib/img_name ') as f:
        # f.write(data)

if __name__ == "__main__":
    for i in range(1,11):
        print('第%d次'%i)
        url = 'http://pic.netbian.com/4kmeinv/'
        url_list = url + 'index_%d.html'%i
        print(url_list)
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }
        response = requests.get(url=url_list, headers=headers)
        # 手动设定响应数据的编码格式
        # response.encoding = 'utf-8'
        page_text = response.text
        # print(page_text)

        #数据解析：src的属性值  alt属性
        tree = etree.HTML(page_text) 
        # print(tree)  ##返回一个类似编码的东西 <Element html at 0x23121875648>
        li_list = tree.xpath('//div[@class="slist"]/ul/li')
        # print(li_list) ##返回一个列表：格式是 Element li at 数字


        #创建一个文件夹
        if not os.path.exists('./picLibs'):
            os.mkdir('./picLibs')

        for li in li_list:
            img_src = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
            img_name = li.xpath('./a/img/@alt')[0]+'.jpg' ##中文名字会乱码，一般要.encode('iso-8859-1').decode('gbk')

    #         #通用处理中文乱码的解决方案
            img_name = img_name.encode('iso-8859-1').decode('gbk')

            print(img_name,img_src)
            # 请求图片进行持久化存储
            img_data = requests.get(url=img_src, headers=headers).content ##一般照片为：main.get(url=url,heards=heards).content
            img_path = 'picLibs/'+img_name
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name, '下载成功！！！')
    print('------------------------OVER!---------------------------------')