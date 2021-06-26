####将本部分代码复制到上一节代码之后，因为要调用上述封装的tranformImgCode方法

session = requests.Session()

# 识别验证码图下载
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
page_text = session.get(url=url, headers=headers).text
# 解析验证码图片的地址
tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.org' + tree.xpath('//*[@id="imgCode"]/@src')[0]
# 将验证码图片保存本地
img_data = session.get(img_src, headers=headers).content
with open('./code.jpg', 'wb') as fp:
	fp.write(img_data)

# 识别验证码
code_text = tranformImgCode('./code.jpg', 1902)
print(code_text)
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data = {
	'__VIEWSTATE': 'f1ECt6+6MPtdTZMJtYOYS/7ww2d/DPy9t8JQcIt1QuOneLTbNQuYqPcCjZNbDAbfb9vj3k6f0M7EKTf0YqElM1k1A5ELwyTvUzBii+9LDRBbIMmc/jb0DJPsYfI=',
	'__VIEWSTATEGENERATOR': 'C93BE1AE',
	'from': 'http://so.gushiwen.cn/user/collect.aspx',
	'email': '账号',
	'pwd': '密码',
	'code': code_text,  # 动态变化
	'denglu': '登录',
	}
# 对点击登录按钮发起请求
page_text_login = session.post(url=login_url, headers=headers, data=data).text
with open('./gushiwen.html', 'w', encoding='utf-8') as fp:
	fp.write(page_text_login)