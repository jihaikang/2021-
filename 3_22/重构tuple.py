'''可变序列   列表、字典'''
lst = [10,20,45]
lis = [1,2,3]
print(id(lst))
lis1 = lst + lis # 加号的作用可真多，这都比得上extend()方法了
print(lis1,id(lis1))
lst.append(300) # append方法不改变id，且加入一个元素在其最后
print(id(lst))
a = [100,]
lst.extend(a) #expend方法
print(id(lst)) # 有点毒啊,extend()方法也没有改变id
'''不可变序列   字符串、元组'''
s = 'hello'
print(id(s))
s = s+'world' # 字符串加字符串Id不变,多次尝试不同字符串相加会不变
print(id(s))
print(s)


'''元组的创建方式'''
#第一种使用小括号
t = ('Python','hello',98)
a = (10,20,98)
print(a[2] in t)
print(type(t))

t0 = 'Python','hello',98
print(t0)
print(type(t0))

t3 = ('Python',)     #如果元组中只有一个元素，逗号不能省略
print(t3)
print(type(t3))


#第二种使用内置函数tuple
t1 = tuple(('Python','hello',98))
print(t1)
print(type(t1))

'''空元组的创建方式'''
lst =[]
lst1= list()

d={}
d2=dict()

t4=()
t5=tuple()

print('空列表',lst,lst1)
print('空字典',d,d2)
print('空元组',t4,t5)

t = (10,[20,30],9)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
'''尝试将t[1]修改为100'''
print(id(100))
#t[1]=100    #元组是不允许修改元素的
'''由于[20,30]是列表，而列表是可变序列，所以可以向列表中添加元素，而列表的内存地址不变'''
t[1].append(100)   #向列表中添加元素
print(t,id(t[1]))
# print(t,id(t[1]))

'''元组的遍历'''
t = ('Python','world',98)
'''第一种获取元组元素的方式，使用索引'''
print(t[0])
print(t[1])
print(t[2])
#print(t[3])   #IndexError
'''遍历元组'''
for item in t:
  print(item)

'''元组的遍历'''
t = ('Python','world',98)
'''第一种获取元组元素的方式，使用索引'''
print(t[0])
print(t[1])
print(t[2])
#print(t[3])   #IndexError
'''遍历元组'''
for item in t:
  print(item)

