import os
from datetime import datetime # 导入时间函数

if not os.path.exists('./6_7'): # 创建文件夹
    os.mkdir('./6_7')
fp = open('暂时.txt','a',encoding = 'utf-8') # 创建文件 ，类型.txt.(a,w均可文件不存在时创建新的文件，且把写入的字符串加入到文件末尾)

a = datetime.now()  # 获取当前时间,类型位<class 'datetime.datetime'>
# print(a) # 打印现在的时间
# print(type(a))
time_now = a.strftime("%A, %d. %B %Y %I:%M%p") # 时间格式化，类型为
# print(time_now)
# print(type(time_now))
# print(a)
# time_now = str(a)
fp.writelines(time_now+'\n') # 写入时间 weitelines 我用'\n'符加入进去还是一列