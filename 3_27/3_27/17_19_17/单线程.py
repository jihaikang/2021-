import time
#使用单线程串行方式执行
def get_page(str):
    print('正在下载：',str)
    time.sleep(2)
    print('下载成功：',str) # 单线程就类似面向过程那样,一步执行完之后才能执行下一步
    
name_list = ['xiaozi','aa','bb','cc']
start_time = time.time()
for i in range(len(name_list)):
    get_page(name_list[i])
end_time = time.time()
print('%d second' % (end_time-start_time))