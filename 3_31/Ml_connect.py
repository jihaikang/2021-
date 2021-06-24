from pymysql import *

# conn=connect('localhost','3306','db_student','root','1024jihaikang') 看看别人的再看看你的
conn = connect(host='localhost',port=3306,database='school',user='root',password='1024jihaikang',charset='utf8')
 # 获得Cursor对象
cs1 = conn.cursor()

print(cs1) # 这打印出来的返回的是 <pymysql.cursors.Cursor object at 0x000001ED7DC90470>
# conn.close()
# count = cs1.execute('update tb_student set stuname='白过' where stuname='杨过'')

# conn.commit()