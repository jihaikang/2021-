from tkinter import*
from tkinter.ttk import*
import time

ck=Tk()
ck.title("测试")
ck.geometry("500x300")

e=Text(ck)
e.pack()
a=5
c=[]
b=[0,1,2,3,4,5,6,7,8,9]
for i in c:
        c.append(i)

def q():
        time.sleep(3)
        e.delete(0.0,END)
        for i in b:
                e.insert(END,i)
                e.insert(END,'\n')

while a>0:
        b.pop()
        q()
        time.sleep(3)
        a=a-1
        print(b)

ck.mainloop()