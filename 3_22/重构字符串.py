'''字符串的驻留机制'''
# a = 'Python'
# b = "Python"
# c = '''Python'''
# print(a,id(a)) # 字符串相同，不管赋值给他的变量是什么，他们的内存地址id都将相同
# print(b,id(b))
# print(c,id(c))

# 用is判断字符串是不是同一个id
# a = 'abc'
# b = 'ab'+'c' # 字符串拼接时建议使用join,效率高，且创建一个新对象得内存空间
# c = ''.join(['ab','c'])
# print(id(a),id(c),id(b)) 
# print(c,type(c))
# print(a,type(a))
# print(a is b)
# print(c is  a) #  is用法用来判断两者是不是属于同一个内存地址
# import sys
# a = 'abc%'
# b = 'abc%'
# print(a is b)
# a = sys.intern(b) # .intern方法并不改变内存地址，intern方法强制2个字符串指向同一个对象
# print(a is b)

#字符串的查询操作
# s = 'hello.hello'
# #index查找子串第一次出现的位置，如果查找子串不存在，抛出ValueError
# print(s.index('lo'))	#3
# #查找子串第一次出现的位置，如果查找子串不存在，则返回-1
# print(s.find('lo'))		#3
# #查找子串最后一次出现的位置，如果查找子串不存在，抛出ValueError
# print(s.rindex('lo'))	#9
# #查找子串最后一次出现的位置，如果查找子串不存在，则返回-1
# print(s.rfind('lo'))	#9
# #print(s.index('k'))   	#ValueError
# print(s.find('k'))    	#-1
# #print(s.rindex('k'))
# print(s.rfind('k'))

# 字符串得大小写转换
# '''字符串中的转换'''
# s = 'hello,python'
# a = s.upper()		#全部转换大写，产生一个新的字符串对象
# print(a,id(a))
# print(s,id(s))
# b = s.lower()		#全部转换小写，产生一个新的字符串对象
# print(b,id(b)) 
# print(s,id(s))
# print(b == s)
# print(b is s)		#False
# s2 = 'hello,Python'
# print(s2.swapcase())	#字符串所有大写转换为小写.所有小写转换为大写
# print(s2.capitalize())  #把第一个字母转换为大写，其余字母转换为小写
# print(s2.title())		#把每个单词的第一个字母转换为大写，把每个单词的剩余字母转换为小写

# 字符串对齐操作

# center		ljust		rjust		zfill
# s = 'hello,Python'

# #居中对齐，第一个参数指定宽度，第二个参数指定填充符，默认空格。若设置宽度小于实际宽度，返回原字符串
# print(s.center(20,'*')) # 这都是打印出来的对齐啊

# #左对齐，第一个参数指定宽度，第二个参数指定填充符
# print(s.ljust(20,'*'))
# print(s.ljust(13))
# print(s.ljust(20))

# #右对齐
# print(s.rjust(20,'*'))
# print(s.rjust(20))
# print(s.rjust(13))

# #右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串宽度
# print(s.zfill(20))
# # print(s.zfill(10))
# print('-8910'.zfill(8))  #减号后开始添0 看不懂他的作用，为什么是减号后添加0

# # split	左劈分,不指定sep=符号时，默认空格劈分号，返回一个新的列表	rsplit  字符串的劈分操作 右劈分
# s = 'hello world Python'
# # '''split从字符串的左边开始劈分，默认的劈分字符是空格字符，返回的值都是一个列表'''
# lst = s.split()
# print(lst)
# s1 = 'hello|world|Python'
# print(s1.split(sep = '|'))		#通过参数sep指定劈分符
# print(s1.split(sep = '|',maxsplit = 2))		#通过maxsplit指定劈分字符串时最大劈分次数，经过最大次劈分后，剩余子串会单独作为一部分

# # '''rsplit从字符串的右边开始劈分，默认的劈分符是空格字符串，返回的值都是一个列表'''
# # print(s1.rsplit())
# # print(s1.rsplit(sep = '|'))
# # print(s1.rsplit(sep = '|',maxsplit = 1))

# # 判断字符串是否是符合某一标准
# # 指定字符串的操作
# # isidentifier合法的标识符		isspace	由空白字符组成（回车、换行、水平制表符）	isalpha		isdecimal		isnumeric	isalnum
# #判断指定的字符串是不是合法的标识符
# s = 'hello,python'
# print('1.',s.isidentifier()) # 加，号就不是合法得标识符了for str
# print('2.','hello'.isidentifier())
# print('3.','张三_'.isidentifier())
# print('4.','123张三_'.isidentifier())

# # #判断指定的字符串是否全部由空白字符组成（回车、换行、水平制表符）	isspace	
# print('5.','\t'.isspace())

# # #判断指定的字符串是否全部由字母组成isalpha
# print('6.','abc'.isalpha())
# print('7.','张三'.isalpha()) # 中文在字符串中也算字母么
# print('8.','张三1'.isalpha())

# # #判断指定的字符串是否全部由十进制数字组成	isdecimal
# print('9.','123'.isdecimal())
# print('10.','123四'.isdecimal())
# print('11.','ⅠⅡⅢ'.isdecimal())

# # #判断指定的字符串是否全部由数字组成	isnumeric	
# print('12.','123'.isnumeric())
# print('13.','123四'.isnumeric()) #四是数字但不是十进制
# print('14.','ⅠⅡⅢ'.isnumeric())# ⅠⅡⅢ是数字但不是十进制

# # #判断指定的字符串是否全部由字母和数字组成 isalnum
# print('15.','abc1'.isalnum())
# print('16.','张三123'.isalnum())
# print('17.','abc!'.isalnum())

# 替换字符串
# repalce替换字符串.repalce（'self',replaceself,times）		join列表元组变字符串
#replace第一个参数指定被替换子串，第二个参数指定替换子串，第三个参数指定最大替换次数
# s = 'hello,Python'
# print(s.replace('Python','Java'))
# s1 = 'hello,Python,Python,Python'
# print(s1.replace('Python','Java',3))

# # 类似于魔法的操作了
# #join将列表或元组中的字符串合并为一个字符串
# lst = ['hello','java','Python']
# print(type('|'.join(lst)))  #变成了字符串
# print(''.join(lst))

# t = ('hello','java','Python')
# print(''.join(t))

# print('*'.join('Python'))


# ord asill转十进制 chr十进制转other decode
# 字符串的比较
# print('apple' == 'apple')	#这里要用==,==是比较是否相等,而=是赋值#True
# print('apple' > 'banana')   #97>98,Flase
# print(ord('a'),ord('b'))
# print(ord('杨'))

# print(chr(97),chr(98))
# print(chr(2666))

# '''is与 == 的区别
# ==比较的是value
# # is 比较的是id'''
# a = b = 'Python'
# c = 'Python'
# print(a == b) # True
# print(b == c) # True
# print(a is b) # True
# print(a is c) # True
# print(id(a)) # True
# print(id(b)) # True
# print(id(c)) # True

# 字符串的切片[start:end:step];切片均是用[]
# s = 'hello,Python'
# s1 = s[:5]		#没有指定起始位置，从0开始
# s2 = s[6:]		#没有指定结束位置，直到最后一个为止
# s3 = '!'
# newstr = s1 + s3 + s2
# print(s1)
# print(s2)
# print(newstr)
# print(id(s))
# print(id(s1))
# print(id(s2))
# print(id(s3))
# print(id(newstr))

# print('---------切片[start:end:step]------')
# print(s)
# print(s[1:5:1])		#从1开始截到5，不包括5，步长为1
# print(s[::3])		#默认从0开始，直到最后一个元素，索引间隔为2
# print(s[::-1])		#默认从最后一个元素开始，直到第一个元素结束，因为步长为-1
# print(s[-6::-1])		#截取Python字符串,这个包括了最后一个end元素,直到第一个元素结束end不写就包含end

# 三种格式化字符串的方式
# '''格式化字符串'''%作占位符；{}作占位符,format
#使用 % 占位符
# name = '张三'
# age = 20
# print('我叫%s，今年%d岁' % (name,age))

# #使用 {} 占位符
# print('我叫{0}，今年{1}岁'.format(name,age))

# #f-string（Python 3.x以上版本）
# print(f'我叫{name}，今年{age}岁')

# #宽度和精度
# print('%d' % 99)
# print('%10d' % 99)			#10代表宽度
# print('%.3f' % 3.1415926)	#.3保留三位小数
# print('%10.3f' % 3.1415926)	#宽度为10，小数点后三位

# print('{0}'.format(3.1415926))
# print('{0:.3}'.format(3.1415926))	#.3表示一共是3位数
# print('{0:.3f}'.format(3.1415926))	#.3f表示3位小数
# print('{:10.3f}'.format(3.1415926))	#同时设置宽度和精度，一共是10位数，3位小数

# # 字符串的编码encode为二进制 解码decode为字符串

# s = '天涯共此时'
# #编码
# print(s.encode(encoding = 'GBK'))	#GBK编码格式中，一个中文占两个字节
# print(s.encode(encoding = 'UTF-8'))	#UTF-8中，一个中文占三个字节

# #解码
# byte = s.encode(encoding = 'GBK')		#编码
# print(byte.decode(encoding = 'GBK'))	#解码   byte代表的就是一个二进制数据（字节类型的数据）

# byte = s.encode(encoding = 'UTF-8')		#编码
# print(byte.decode(encoding = 'UTF-8')) # decode解码要已经知道该字符串是什么编码，而常用的字符串已经是utf-8编码了，所以不需要使用decode解码了