#导入线程池模块对应的类
import time
from multiprocessing.dummy import Pool

#使用线程池方式执行
start_time = time.time()
def get_page(str):
    print('正在下载：', str)
    time.sleep(2)
    print('下载成功：', str)

name_list = ['xiaozi','aa','bb','cc']

#实例化一个线程池对象
pool = Pool(4)      #线程池开辟4个线程 Pool是个方法
#将列表中每一个列表元素传递给get_page进行处理
pool.map(get_page, name_list) #.map(hanshu,liebiao)可把列表中的值一个一个传经去，可是他又没用循环编列怎么可以提取列表的一个一个值

end_time = time.time()
print(end_time - start_time)