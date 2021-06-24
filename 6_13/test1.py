
# a=[[1,2,3],[4,5,6],[7,8,9]]
# s=0
# for c in a:
#     print('c是什么：{}'.format(c))
#     for j in range(3):
#         print('j是什么：{}'.format(j))
#         s=c[j]+s  # 双列表的启示难道只有能够相加么 双列表循环打印出元素：把3变为len(c)
# print(s)


# from django.contrib.auth.models import User

# user=User.objects.create_user(username='c语言中文网',password='123456',email='664104694@qq.com')
# user.save()#调用该方法保存数据 

# user.set_password(password='12345abc')#会对原密码进行修改


# from django.contrib.auth import authenticate  # auth 模块提供了认证用户功能

# user = authenticate(username='c语言中文网',password='12345abc')


# user.user_permission.add(permission)#给某个用户权限的添加权限
# group = Group.objects.create(name=group_name)#添加新的用户组
# group.save() #保存新建好的用户组
# group.delete()#删除用户组


# import urllib.request
# import urllib.parse

# # http 500报错


# header = {'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}

# url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'   #这个链接是我从网页里复制出来的，和书里的不太一样
# data = {}  # 原来字典加入参数是直接加，不用函数，不用考虑替代，键相同才会替代
# data['type'] = 'AUTO'
# data['i'] = 'I LOVE FISHC.COM'
# data['doctype'] = 'json'
# data['xmlVersion'] = '2.1'    #书上的是1.6，但是网页里的是2.1，应该是版本有更新了
# data['keyfrom'] = 'fanyi.web'
# data['ue'] = 'UTF - 8'
# data['typoResult'] = 'true'
# data = urllib.parse.urlencode(data).encode('UTF - 8')
# print(data)
# response = urllib.request.urlopen(url,data)
# html = response.read().decode('UTF -8')
# print(html)



# 有道翻译
# import urllib.request
# import urllib.parse
# import json
# import time

# # 有道翻译js中post请求传递的参数有哪些，怎么查找

# while True:
#       content = input("请输入要翻译的内容：(输入”q!”退出程序):")
#       if content == "q!":
#             break

#       url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult"

#       head = {}
#       head['User.Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
#       data = {}
#       data["i"] = content
#       data["from"] = "AUTO"
#       data["to"] = "AUTO"
#       data["smartresult"] = "dict"
#       data["client"] = "fanyideskweb"
#       data["salt"] = "15981872159194"
#       data["sign"] = "cfd7bc0ad5a9d4433c3ff54e338c61f9"
#       data["lts"] = "1598187215919"
#       data["bv"] = "4b1009b506fa4405f21e207abc4459fd"
#       data["doctype"] = "json"
#       data["version"] = "2.1"
#       data["keyfrom"] = "fanyi.web"
#       data["action"] =" FY_BY_REALTlME"
#       data = urllib.parse.urlencode(data).encode("utf-8")

#       response = urllib.request.urlopen(url,data)
#       html = response.read().decode("utf-8")

#       target = json.loads(html)
#       print("翻译结果：%s"%(target["translateResult"][0][0]["tgt"]))
#       time.sleep(5)

# from tkinter import *
# root=Tk()
# mylist=[x for x in range(100)]
# sb=Scrollbar(root) # sb是Scrollbar（滚动条）的一个实例
# sb.pack(side=RIGHT,fill=Y)
# thelist=Listbox(root,yscrollcommand=sb.set)
# thelist.pack()
# for j in mylist:
#     thelist.insert(END,j)
# Button(root,text='删除',command=lambda x=thelist:x.delete(ACTIVE)).pack(side=LEFT)

# sb.config(command=thelist.yview)  # 实现滚动条的功能。

# mainloop()  # 消息循环入口



# while True:
#     a = int(input('请输入一个整数：'))
#       #input函数得到的是个字符串 所以a是字符串 直接加int也可以
#     # a = int(a)
#     print(a)
#     b = isinstance(a, int)
#     if b == True:
#         print('输入正确。')
#     else:
#         print('输入错误。')


'''
要求1：实现获取、设置和删除一个元素的行为（删除一个元素的时候对应的计数器也会被删除）
要求2：增加 counter(index) 方法，返回 index 参数所指定的元素记录的访问次数
要求3：实现 append()、pop()、remove()、insert()、clear() 和 reverse() 方法（重写这些方法的时候注意考虑计数器的对应改变）
'''

class CountList:
    def __init__(self,*args): # *args是元组把 *args是非关键字参数，用于元组，**kw是关键字参数，用于字典
        self.values=[x for x in args]  # 把x从列表中导出
        self.count={}.fromkeys(range(len(self.values)),0) #自己定义count方法 创建字典 fromkeys() 函数用于创建一个新字典
        self.stack=dict()
        self.rvalues=list()
    def __len__(self):
        return len(self.values)
    def __getitem__(self,key):
        self.count[key]+=1
        return self.values[key]
    def __delitem__(self,key):
        del self.count[key]
        del self.values[key]
    def counter(self,key):
        return self.count[key]
    def append(self,key):
        self.values=self.values+[key]
        self.count[len(self.values)-1]=0
    def pop(self):  # 求问导致pop(self)在类中运行失效的原因是什么？
        return self.values[len(self.values)-1]
        del self.count[self.values[len(self.values)-1]]  # vscode中黑的代码是无法运行的
        del self.values[len(self.values)-1]
    def remove(self,key):
        self.stack=self.count
        self.rvalues=self.values
        for i in range(len(self.values)):
            try:
                if self.values[i]==key:
                    del self.rvalues[i]
                    del self.stack[i]
            except IndexError:
                pass
        self.count=self.stack
        self.values=self.rvalues
        self.stack=dict()
        self.rvalues=list()
    def insert(self,index,key):
        self.values=self.values[:index]+[key]+self.values[index:]
        for i in range(len(self.values)):
            if i<index:
                self.stack[i]=self.count[i]
            elif i==index:
                self.stack[i]=0
            else:
                self.stack[i]=self.count[i-1]
        self.count=self.stack
        self.stack=dict()
    def clear(self):
        self.count=dict()
        self.values=list()
    def reverse(self):
        for i in range(len(self.values)-1,-1,-1):
            self.rvalues.append(self.values[i])
            self.stack[len(self.values)-1-i]=self.count[i]
        self.values=self.rvalues
        self.count=self.stack
        self.rvalues=list()
        self.stack=dict()


c1=CountList(0,1,2,3)
c1[1]  # 这啥玩意没看懂
c1[2]
c1[2]
c1[3]
c1[3]
c1[3]
c1.append(4)
c1[4]
c1[4]
c1[4]
c1[4]

print(c1.values)
print(c1.count)