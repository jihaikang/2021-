# import random

# # 3种方式创建字典
# '''使用{}创建字典'''
# scores = {'张三':100,'李四':98,'王五':45}
# print(scores)
# print(type(scores))
# '''使用内置函数dict'''
# student = dict(name='jack',age=20,) # 使用dict方式构成字典：dict(name='',name1 = '')
# print(student)
# '''空字典'''
# d = {}
# print(d)
# # 直接赋值法
# stuInfo = {}
# for i in range(20):
#     name = 'westos' + str(i)
#     score = random.randint(60,100)
#     stuInfo[name] = score
# '''获取字典中的值'''
# scores = {'张三':100,'李四':98,'王五':45}
# ''' 第一种方式，使用[]'''
# print(scores['张三'])
# # print(scores['陈六'])         #KeyError
# '''第二种方式 使用get'''
# print(scores.get('张三'))
# print(scores.get('陈六'))     #查询不到返回None
# print(scores.get('张三',99))  #99是在查找麻七对应的value不存在时，提供的一个返回值


# '''key的判断'''
# scores = {'张三':100,'李四':98,'王五':45}
# b = {'李四':98}
# # print(b in scores) #整个字典不行TypeError: unhashable type: 'dict'
# print('张三' in scores)
# print('张三' not in scores)

# del scores['张三']    # 删除指定的key-value对
# #scores.clear()      #清空字典元素
# print(scores) # 这因该报错 没有该对象
# scores['陈六'] = 98   #新增元素   scores可以查询直接的值，也可以添加改变值 查询:scores['key'];改变：scores['key']= values
# print(scores)
# scores['陈六'] = 100  #修改元素
# print(scores)


# scores = {'张三':100,'李四':98,'王五':45}
# #获取所有的key
# keys = scores.keys()
# print(keys)
# print(type(keys))
# print(list(keys))  #将所有的key组成的视图转成列表
# #获取所有的Value
# values = scores.values()
# print(values)
# print(type(values))
# print(list(values))
# print(str(values))
# print(tuple(values))
# # items获取所有的key-value对 
# items = scores.items() # items获取的是字符串
# print(items)  
# print(type(items)) # 这个生成的类型是<class 'dict_items'>
# print(type(tuple(items))) #加元组括号也是 <class 'dict_items'>,用tuple方法则变成了<class 'tuple'>
# print(type([items]))   

# # 字典元素的遍历
# scores = {'张三':100,'李四':98,'王五':45}
# for item in scores:
#   print(item,scores[item],scores.get(item))
#   print('-----------------------')
#   print(scores.get(item))

# d = {'name':'张三','name':'李四'} # key相同，后面的key输出
# print(d)

# d = {'name':'张三','nikename':'张三'} # value相同，还是和平常一样全部输出
# print(d)



# # 字典生成试
# items = ['Fruits','Books','Others']
# prices = [96,78,85,100,120]
# # 2个列表在zip(2个列表)
# d = {item.upper():prices  for item,prices in zip(items,prices)} # .upper用法全部转化为大写
# print(d)


# # 20个学生找出90分以上的人
# stuInfo = {}
# for i in range(20):
#     name = 'westos' + str(i)
#     score = random.randint(60,100)
#     stuInfo[name] = score
# print(stuInfo)

# # 这个表达式也有点东西
# highscore ={}
# for name,score in stuInfo.items():
#     if score >90:
#         highscore[name]= score
# print(highscore)
# print({name:score for name,score in stuInfo.items() if score >90})  # 从后往前看

# if score >90:
#     for name,score in stuInfo.items(): #items获取的是字符串
#         print({name:score})