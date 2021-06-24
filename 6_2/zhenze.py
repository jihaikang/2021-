'''正则练习'''
import re

# 搜搜字符串，以列表类型返回全部能匹配的子串
# 提取出python
print('+'*100)
key = "javapythonc++php"
a=re.findall('python', key)[0]
print(a)

#提取出hello world
print('+'*100)
key = "<html><h1><hello world><h1></html>"
a=re.findall('h1>(.*)<h1', key)
print(a)
#提取170
print('+'*100)
string = '我喜欢身高为170的女孩' # 提取数字
a=re.findall('\d+', string)
print(a)
#提取出http://和https://
print('+'*100)
key = 'http://www.baidu.com and https://boob.com'
a=re.findall('https?://', key) # 提取单个该字符或没有该字符
print(a)
#提取出hello
print('+'*100)
key = 'lalala<hTml><hello></HtMl>hahah' 	#输出<hTml><hello></HtMl>
a=re.findall('<[Hh][Tt][mM][lL]>(.*)</[Hh][Tt][mM][lL]>', key) # 右边的\是转义字符，左边的/是啥
print(a)
#提取出hit.
print('+'*100)
key = 'bobo@hit.edu.com'	#想要匹配到hit
a=re.findall('h.*?\.', key)
print(a)
#匹配sas和saas
print('+'*100)
key = 'saas and sas and saaas'
a=re.findall('sa{1,2}s', key)
print(a)