# 构建列表的方法
# lst = ['hello','world',98]         #使用中括号创建列表
# print(lst[0])
# #使用内置函数list()创建列表 list :需要[],且需加引号如果是字符串的话；单个引号的内容不需要加[]；
# # 常使用方法：name = list(['所需要的值',])
# lis2 = list(['world',97])  
# print(lis2)

# index篇
# lst = ['hello','world',98,'hello']
# print(lst.index('hello'))    #列表存在多个相同元素，只返回列表第一个索引
# #print(lst,index('Python'))   #查询元素不存在ValueError:'Python' is not in list
# #print(lst,index('hello',1,3)) ValueError
# print(lst.index('hello',1,4))  #指定在start到stop之间进行查找

# 列表切片
# lst = [10,20,30,40,50,60,70,80]
# print(lst[1:-2:1])    #start=1 stop=6 step=1切片切出一个新列表
# print('原列表',id(lst))
# lst2 = lst[1:6:1]
# print('切的片段:',id(lst2))
# print(lst[1:6])
# print(lst[1:6:])    #step不写默认从1开始
# print(lst[1:6:2])
# print(lst[:6:2])    #start不写默认从0开始
# print(lst[1::2])    #stop不写默认最后一个元素
# print('--------------step为负数的情况-------------')
# print('原列表：',lst)
# print(lst[-1::-1])
# print(lst[-1::-1])
# print(lst[-2:0:-2])

# 列表的遍历与嵌套
# python = [(1,'sss'),1]
# lst = [10,20,python,'hello']
# # for item in lst:
# #   print(item)
# a = lst[2]
# print(a)
# for i in a:
#     print(i)


# 列表的增加
#向列表的末尾添加一个元素
# lst = [10,20,30]
# print('添加元素之前',lst)
# lst.append(100)
# print('添加元素之后',lst,id(lst))
# lst2 = ['hello','world']
# lst.append(lst2)        #将lst2作为一个元素添加到列表的末尾
# print(lst)
# lst.extend(lst2)        #向列表的末尾一次性添加多个元素  
# print(lst)
# lst.insert(1,lst2)        #在任意位置添加一个元素
# print(lst)
# lst3 = [True,False,'hello']
# # lst = [10, ['hello', 'world'], 20, 30, 100, ['hello', 'world'], 'hello', 'world']
# # lst3 = [True,False,'hello']
# lst[3:] = lst3    
# #[10, ['hello', 'world'], 20, True, False, 'hello']
# #切片替换 这应该是魔法吧 
# print(lst)

# 列表的删除操作
# lst = [10,20,30,40,50,60,30,30]
# a = [10,20,30,40,50]
# print(a[4] in lst)
# lst.remove(30)          #重复元素只删除第一个
# print(lst)
# #lst.remove(100)         #移除元素不存在ValueError
# #pop根据索引移除元素
# lst.pop(1)
# print(lst)
# #lst.pop(8)              #IndexError
# lst.pop()                #默认删除最后一个元素
# print(lst)
# print('-------切片操作删除至少一个元素，将产生一个新的列表对象-----------')
# new_lst = lst[1:3]
# print('原列表',lst)
# print('新列表',new_lst)
# '''不产生新的列表对象，而是删除原列表的内容'''
# lst[1:] = []
# print(lst)
# '''清除列表中的所有元素'''
# lst.clear()
# print(lst)
# '''del语句将列表对象删除'''
# del lst
# 下面是错误的 name 'lst' is not defined
# print(lst) 
# print(type(lst))

# 列表排序
# lst = [20,40,10,98,54]
# print('排序前的列表',lst,id(lst))
# #调用列表对象的sort方法，默认升序
# lst.sort()
# print('排序后的列表',lst,id(lst))
# #指定参数进行降序
# lst.sort(reverse = True)
# print(lst)
# lst.sort(reverse = False)
# print(lst)
# print('-------调用内置函数sorted()对列表对象进行排序，产生一个新的列表对象----')
# lst = [20,40,10,98,54]
# print('原列表',lst)
# new_lst = sorted(lst)
# print(lst,id(lst))
# print(new_lst,id(new_lst))
# desc_lst = sorted(lst,reverse =True)
# print(desc_lst,id(desc_lst))


# 常见的列表生成方式
# lst = [i for i in range(1,10)]
# lst1 = [i*i for i in range(1,10)] # 格式为name = [i for i i range()]
# print(lst)
# print(lst1)
# '''列表中的元素的值为2 4 6 8 10 '''
# lst2 = [i*2 for i in range(1,6)]
# print(lst2)
# lst3 = [i*3 for i in range(1,6)]
# print(lst3)

# 匿名函数
# a= lambda x,y: x*y
# print(a)

