# 源url失效了，要自己来

import requests, bs4, json, os,webbrowser
class PDDGoodsInfo():
    #今天教大家如何爬取PDD商品数据,涉及到,json xml等知识
    def __init__(self, goods_id,token=''):
        '''
        拼多多商品素材下载类
        :param goods_id: 商品id或者商品链接
        :param cookie: PDDAccessToken
        '''
        self.goods_url = f'https://mobile.yangkeduo.com/goods.html?goods_id={goods_id}'
        #这个token就是身份.如果电脑被检测出频繁了,就需要填这个.需要自己去登入一下,一般情况下不需要获取办法,下方有
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'cookie': 'PDDAccessToken='+token}
        res = requests.get(self.goods_url, headers=self.headers)
        text = res.text.split('window.rawData=')[-1].split(''';
    </script>''')[0]
        self.js = json.loads(text)
 
    def get_mallName(self):
        '''
        获取店铺名
        :return:
        '''
        try:
            return self.js['store']['initDataObj']['mall']['mallName']
        except:
            return ''
 
    def get_title(self):
        '''
        获取商品标题
        :return:
        '''
        try:
            return self.js['store']['initDataObj']['goods']['goodsName']
        except:
            return ''
 
    def get_viewImageData(self):
        '''
        获取轮播图列表数据
        :return:
        '''
        try:
            return self.js['store']['initDataObj']['goods']['viewImageData']
        except:
            return ''
 
    def get_detailGallery(self):
        '''
        获取详情图
        :return:
        '''
        try:
            return self.js['store']['initDataObj']['goods']['detailGallery']
        except:
            return ''
 
    def get_videoGallery(self):
        '''
        获取主图视频
        :return:
        '''
        try:
            return self.js['store']['initDataObj']['goods']['videoGallery']
        except:
            return ''
 
    def get_descVideoGallery(self):
        '''
        获取详情视频
        :return:
        '''
        try:
            return self.js['store']['initDataObj']['goods']['descVideoGallery']
        except:
            return ''
 
    def get_sku_img(self):
        '''
        获取sku信息
        :return:
        '''
        try:
            skus = self.js['store']['initDataObj']['goods']['skus']
            l = []
            for item in skus:
                d = {}
                d['src'] = item['thumbUrl']  # 图片地址
                d['specs'] = item['specs']  # 组合,可能是个列表
 
                d['normalPrice'] = item['normalPrice']  # 正常价格
                d['groupPrice'] = item['groupPrice']  # 拼团价格
                name = ''  # sku标题
                for it in item['specs']:
                    name = name + it['spec_key'] + '_' + it['spec_value'] + '_'
                d['name'] = name[:-1]  # 去掉最后一个_
                l.append(d)
            return l
        except:
            return ''
 
    def download_img(self, src, path):
        res = requests.get(src)
        with open(path, 'ab')as f:
            f.write(res.content)
 
    def download_all_data(self):
        # 首先获取数据
        title = self.get_title()
        viewImageData = self.get_viewImageData()  # 商品轮播图
        detailGallery = self.get_detailGallery()  # 商品详情图
        videoGallery = self.get_videoGallery()  # 商品轮播视频
        descVideoGallery = self.get_descVideoGallery()  # 商品详情视频
        skuImg = self.get_sku_img()
        if title == '':
            print('cookie失效!请按照下方教程重新获取Token,或者过一会再试!')
 
            return False
 
 
        # 创建目录
        try:
            os.mkdir(title)
        except:
            pass
        try:
            os.mkdir(f'{title}\\商品轮播图')
        except:
            pass
        try:
            os.mkdir(f'{title}\\商品详情图')
        except:
            pass
        try:
            os.mkdir(f'{title}\\SKU图')
        except:
            pass
        try:
            # 下载全部商品轮播图
            for i, item in enumerate(viewImageData):
                suffix = item.split('.')[-1]
                path = f'{title}\\商品轮播图\\{i + 1}.{suffix}'
                self.download_img(item, path)
            print('下载商品轮播图成功!')
        except Exception as err:
            print('下载商品轮播图失败!', err)
        # 下载全部详情图
        try:
            for i, item in enumerate(detailGallery):
                suffix = item['url'].split('.')[-1]
                path = f'{title}\\商品详情图\\{i + 1}.{suffix}'
                self.download_img(item['url'], path)
            print('下载商品详情图成功!')
        except Exception as err:
            print('下载商品详情图失败!', err)
        # 下载轮播视频
        if videoGallery != '' and len(videoGallery) > 0:
            suffix = videoGallery[0]["url"].split('.')[-1]
            path = f'{title}\\轮播视频.{suffix}'
            self.download_img(videoGallery[0]["url"], path)
            print('下载轮播视频成功!')
        # 下载详情视频
        if descVideoGallery != '' and len(descVideoGallery) > 0:
            suffix = descVideoGallery[0]["url"].split('.')[-1]
            path = f'{title}\\详情视频.{suffix}'
            self.download_img(descVideoGallery[0]["url"], path)
            print('下载详情视频成功!')
        # 下载所有sku图
        try:
            for i, item in enumerate(skuImg):
                suffix = item['src'].split('.')[-1]
                path = f'{title}\\SKU图\\{item["name"]}.{suffix}'.replace('*','x').replace('/','除以')
                self.download_img(item['src'], path)
            print('下载所有sku图成功!')
        except Exception as err:
            print('下载所有sku图失败!', err)
        print('完成')
 
#ZSTQ2TEENQAX6WUODEUP7YVZ27TD6VTGNK4KGGWGCZXZBNQPO5CA1104f3c
#229449473937
#我就是频繁了,,今天试了很多 我已经提前登陆了,获取好了 可以了,看懂了吧,源码和成品exe在下方.
if __name__ == '__main__':
    id=input('请输入您要爬取的商品id或者整个链接也行:')
    if len(id)<4:
        input('请不要瞎几把乱输入!')
    else:
        if id.find('goods_id')!=-1 :
            id=id.split('goods_id=')[-1].split('&')[0]
        goods_info = PDDGoodsInfo(id)
        if goods_info.download_all_data()==False:
            'https://mobile.yangkeduo.com/login.html'
            webbrowser.open(f'https://mobile.yangkeduo.com/login.html')
            print('已经被检测为频繁!所以现在已经为您打开了目标商品地址,请在浏览器中登录您的拼多多账号,然后进行如下操作获取token')
            print('图片教程:[img]https://z3.ax1x.com/2021/03/29/cPmcKs.png[/img]')
            print('步骤1:登入成功后按【F12进入调试模式】')
            print('步骤2:点击下方的【Application】栏目')
            print('步骤3:点击下方的【Cookies】选项并且选中下方的链接')
            print('步骤4:找到Name为PDDAccessToken的，复制它的Value(双击可以复制)')
            print('#'*40)
            token=input('准备好了请将PDDAccessToken的Value值粘贴到此处:')
            goods_info = PDDGoodsInfo(id,token)
            goods_info.download_all_data()
            #运行一下看看效果