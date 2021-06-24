import xlrd

# def openWorkbook():
#读取excel表的数据
workbook = xlrd.open_workbook(r'D:/囧包子/Documents/ifma.xlsx')
# sheet = workbook.sheet_by_index(2)#选取需要读取数据的那一页
# rows =sheet.nrows  #获得行数和列数
# cols =sheet.ncols
# print(rows,cols)

#创建一个数组用来存储excel中的数据
#     p= []
#     for i in range(2,rows):
#         d={}
#         for j in range(0,cols):
#             q='%s' % sheet.cell(0,j).value
#             d[q] = sheet.cell(i,j).value
#         ap = []
#         for k,v in d.items():
#             if isinstance(v,float): #excel中的值默认是float,需要进行判断处理，通过'"%s":%d'，'"%s":"%s"'格式化数组
#                 ap.append('"%s":%d' % (k, v))
#             else:
#                 ap.append('"%s":"%s"' % (k, v)) 
#         s = '{%s}' % (','.join(ap))   #继续格式化
#         p.append(s)
#     t ='[%s]' % (','.join(p)) #格式化
#     print (t)
#    
#     with open('student4.json',"w") as f:
#         f.write(t)


# openWorkbook()


# ————————————————
# 版权声明：本文为CSDN博主「井冈山市监人」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/liu943367080/article/details/98759683