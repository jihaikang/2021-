# import os


# with open('a.txt','wb') as fp；
# file = open('a.txt','w',encoding = 'utf-8') # w是覆盖并且重新写入
# file.write('Python') # 文件的杜西呃怎么打印出来是个中文字符
# # print(file.readlines())		#结果是一个list
# file = open('a.txt','r+') # 一定要先读取,才能打印出来
# print(file) # 打印出来的file应该是一个地址之类的
# file.close()


# file = open('b.txt','w') # 创建文件；只写模式打开文件，如果文件不存在则创建；如果文件存在，则覆盖原有内容，指针放在文件开头
# file.write('Python')
# file.close()
# file = open('b.txt','a') # 追加模式打开文件，如果文件不存在则创建，文件指针在文件开头；如果文件存在，则在文件末尾追加内容，文件指针在原文件末尾
# file.write('Python')
# file.close()


# src_file = open(r'D:\百度网盘企业版\a_pactice\3_23\1.jpg','rb') # 打开图片出现问题 ，打开图片的绝对路径or相对路径,我加了/都不行，windows复制过来的路径是\
# target_file = open(r'.\3_23\copy1.jpg','wb') # 加个r 不然会报错 OSError: [Errno 22] Invalid argument:无效参数 
# target_file.write(src_file.read())
# target_file.close()
# src_file.close()
# # with open可以不用自己手动关闭文件释放资源 filename.close()
# with open(r'.\3_23\程潇4k壁纸.jpg','rb') as fp: # 打卡图片的路径有问题 rb图片要以二进制模式打开
#     with open (r'.\3_23\copy1.jpg','wb') as cp:
#         cp.write(fp.read()) # 要把文件可读才能写入么

# 疑惑 为什么file.writelines(lst) # weitelines 写入一个列表 返回的是个空列表
# file = open('a.txt','r')
# print(file.read(2))
# print(file.readline())# 从文本文件中读取一行内容
# print(file.readlines()) # 把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
# file.close()           # 把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关资源
# # with open('c.txt','w',encoding = 'utf-8')
# file = open('c.txt','a+') # 以追加模式打开，若无，则创建，文件指针再开头，已有，文件指针在结尾
# file.write('hello')
# lst = ['java','go','python']
# file.writelines(lst) # weitelines 写入一个列表
# print(file.readlines()) 
# file.close()

# file = open('c.txt','r') # 用r打开就可读,然后打印出来
# file.seek(2)	#一个中文两个字节 设置文件当前位置；offest偏移当前字节的数，.seek(offset[, whence])
# print(file.read())
# print(file.tell()) # 返回文件指针的当前位置
# file.close()

# file = open('c.txt','a')
# file.write('hello')
# file.flush() # 把缓冲区的内容写入文件，但不关闭文件
# file.write('world')
# file.close()

# # with语句
# print(type(open('a.txt','r')))
# with open('a.txt','r') as file:
#     print(file.read())

# '''MyContentMgr实现了特殊方法__enter__(),__exit__()称为该类对象遵守了上下文管理器协议。
# 该类对象的实例对象，称为上下文管理器

# MyContentMgr()'''
# class MyContentMgr(object):
#     def __enter__(self):
#         print('enter方法被调用执行了')
#         return self
    
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         print('exit方法被调用执行了')
        
#     def show(self):
#         print('show方法被调用执行了')
# with MyContentMgr() as file:
#     file.show() # 我以为只会调用show,结果是132.MyContentMgr我的内容管理器


# -------------分隔符-----------------------
# os模块与操作系统相关的一个模块
# 这个是一个一个执行的啊
# os.system('notepad.exe') # 打开记事本
# os.system('calc.exe') # 打开计算机
# # 直接调用可执行文件
# # os.startfile('D:\\YesPlayMusic\\YesPlayMusic.exe')

# print(os.listdir('D:/BaiduNetdiskDownload/Scrapy网络爬虫实战/代码/Chapter2/3_23')	)
# print('----'*20)

# # 目录操作


# print(os.getcwd()) # 返回当前目录信息
# print('----'*20)

# print(os.listdir('3_23'))	#返回当前目录信息和文件信息 	#办公自动化经常使用
# print('----'*20)	


# os.mkdir('newdir2') # 本路径下创建文件夹
# #  os.makedirs('A/B/C') 多路径下创建文件夹
# os.rmdir('newdir2') # 本路径下删除文件夹
# # os.removedirs('A/B/C')  #多路径下删除文件夹

# # os.chdir('F:\\desktop\\chap14') #改变当前工作目录
# print(os.getcwd()) #返回当前工作目录

#  os.path模块
# print(os.path.abspath('moni.py')) # 获取文件目录的绝对路径,不在该目录下则返回False
# print(os.path.exists('demo13.py'),os.path.exists('demo18.py')) #用于判断文件或目录是否存在，如果存在返回True，否则返回False
# print(os.path.join('E:\\Python','demo13.py')) #把文件目录和文件名相拼起来
# print(os.path.split('D:\BaiduNetdiskDownload\Scrapy网络爬虫实战\代码\Chapter2\3_23\文件文本的操作.py')) # 分离目录名与文件名
# print(os.path.splitext('demo13.py')) # 分离文件名和扩展名
# print(os.path.basename('D:\BaiduNetdiskDownload\Scrapy网络爬虫实战\代码\Chapter2\3_23\文件文本的操作.py')) #从一个目录中提取文件名
# print(os.path.dirname('D:\BaiduNetdiskDownload\Scrapy网络爬虫实战\代码\Chapter2\3_23\文件文本的操作.py')) #从一个路径中提取文件路径，不包括文件名
# print(os.path.isdir('D:\BaiduNetdiskDownload') #用于判断是否为路径


# '''列出指定目录下的所有py文件'''
# # import os
# path = os.getcwd()
# lst = os.listdir(path)
# for filename in lst:
#     if filename.endswith('.py'):
#         print(filename)

# 好东西，遍历所有目录及文件夹
# chap15-->newdir-->sub-->遍历所有文件walk
# path = os.getcwd()
# print(path)
# lst_files = os.walk(path)
# for dirpath,dirname,filename in lst_files:
#     print(dirname)
#     print(dirpath)
#     print(filename)
#     print('--------------------------')
#     for dir in dirname:
#         print(os.path.join(dirpath,dir))
        
#     for file in filename:
#         print(os.path.join(dirpath,file))
#     print('+++++++++++++++++++++++++')