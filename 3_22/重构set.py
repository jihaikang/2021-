# # 集合的的特点 1:无序 2：没有重复 3：
# # '''第一种创建方式使用{} ; 集合是没有value值得字典'''
# s = {2,3,4,5,5,6,7,7}	#集合中的元素不允许重复

# print(s)
# '''第二种创建方式使用set{}'''
# s1 = set(range(6))
# print(s1,type(s1))

# s2 = set([1,2,4,5,5,5,6,6]) # 集合中的元素重复后会导致只显示一个重复的元素，不会显示重复的多个元素
# print(s2,type(s2))

# s3 = set((1,2,4,4,5,65))   #集合中的元素是无序的
# print(s3,type(s3))

# s4 = set('Python')
# print(s4,type(s4))

# s5 = set({12,4,34,55,66,44,4})
# print(s5,type(s5))

# #定义一个空集合
# s6 = {}
# print(type(s6)) # 空集合默认是字典

# s7 = set()
# print(type(s7))

# -----------分割线---------------------


# s = {10,20,30,405,60}

# #集合元素的判断操作
# print(10 in s)
# print(100 in s)
# print(10 not in s)
# print(100 not in s)

# #集合元素的新增操作
# s.add(80)        #一次添加一个元素
# print(s)
# s.update({})   #一次至少添加一个元素，不添加元素也不报错就是更新呗
# print(s,type(s))
# s.update([100,99,8]) # 添加其他3中元素，在其内部均变为set集合
# print(s,type(s))
# s.update((78,64,56))
# print(s,type(s))

# #集合元素的删除操作
# s.remove(100)	 #一次删除一个指定元素，元素不存在抛出KeyError
# print(s)
# #s.remove(500)   #KeyError
# s.discard(500)   #删除一个指定元素，元素不存在不报异常
# s.discard(300)
# print(s)
# s.pop()          #一次只能删除一个任意元素
# s.pop()           # pop不指定随便删除集合中的一个元素
# #s.pop(400)      #TypeError 不能够添加参数
# print(s)
# s.clear()        #清空集合
# print(s)


# '''集合的数学操作'''
# #交集 intersection &
# s1 = {10,20,30,40}
# s2 = {20,30,40,50,60}
# print(s1.intersection(s2))
# print(s1 & s2) #交集用&符号 和 .intersection
# print(s1)
# print(s2)

# #并集 union | 
# print(s1.union(s2))
# print(s1 | s2)# 并集use union and |
# print(s1)
# print(s2)

# #差集  difference -
# print(s1.difference(s2))
# print(s1 - s2) # 差集use difference and -
# print(s1)
# print(s2)

# #对称差集  symmetric_difference  ^
# print(s1.symmetric_difference(s2)) # 对称差集 use symmentric_difference and ^
# print(s1 ^ s2)

# '''列表生成式'''
# lst = [i*i for i in range(10)]
# print(lst)

# '''集合生成式'''
# s = {i*i for i in range(10)} # 不同之处在于外括号for set and list
# print(s)