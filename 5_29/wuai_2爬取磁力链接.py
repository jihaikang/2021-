import requests
from lxml import etree
 
search = input("请输入您要查询的关键字（不要有空格/特殊符号）：")
page_num = int(input("请输入需要获取的页数（如:1,2,3）："))
url = "https://www.zhaocili608.xyz/s.php?q={}".format(search)
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
re = requests.get(url=url, headers=head).text
h = etree.HTML(re)
p_next = h.xpath("//tbody/tr[last()]/td/a/text()")[0]  # 下一页（用于判断是否有下一页）
for p in range(1, page_num+1):  # 页码数量
    # 判断是否有下一页
    if "下一页" in p_next:
        page = h.xpath("//tbody/tr[last()]/td/a/@href")[0].replace("//", "https://")  # 页码
        baseurl = page.replace("2.html", "{}.html").format(p)  # 完整页码
    else:
        baseurl = url
    print("--------------正在为您查找（第{0}页）：【{1}】的相关信息--------------".format(p, search))
    r = requests.get(url=baseurl, headers=head).text
    html = etree.HTML(r)
    lst = html.xpath("//tbody/tr/td/a[@target='_blank']")
    # 获取页面每个资源的详情数据
    for i in lst:
        fp = open(search+".txt", "a", encoding="utf-8")  # 持久化存储数据(不覆盖内容)
 
        href = i.xpath("./@href")[0].replace("//", "https://")  # 详情链接
        response = requests.get(url=href, headers=head).text
        tree = etree.HTML(response)
 
        title = tree.xpath("//div[@class='container']//h2/text()")[0]  # 标题
        fp.write("标题：" + title + "\n")  # 写入标题
        print("标题：", title)
 
        data = tree.xpath("//div[@class='container']//div[@class='row']/dl/dd[3]/text()")[0]  # 日期
        fp.write("日期：" + data + "\n")  # 写入日期
        print("日期：", data)
 
        size = tree.xpath("//div[@class='container']//div[@class='row']/dl/dd[4]/text()")[0]  # 文件大小
        fp.write("文件大小：" + size + "\n")  # 写入文件大小
        print("文件大小：", size)
 
        magnet = tree.xpath("//div[@class='container']//div/input/@value")[0]  # 磁力链接
        fp.write("磁力链接：" + magnet + "\n"*2)  # 写入磁力链接
        print("磁力链接：", magnet)
        print()
    # 判断是否有下一页（继续/结束循环）
    if "下一页" in p_next:
        pass
    else:
        print("资源获取完毕！")
        break