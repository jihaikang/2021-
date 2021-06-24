# -*- coding: UTF-8 -*-
import tkinter as tk
import win32com.client as wc
import os, re, glob, time, shutil
from tkinter import filedialog
from bs4 import BeautifulSoup
from pydocx import PyDocX
 
class Doc2Xlsx(object):
        """docstring for Doc2Xlsx"""
        def __init__(self):
                super(Doc2Xlsx, self).__init__()
 
        # doc2docx
        def doc2docx(self, path, file):
                word = wc.Dispatch("Word.Application")
                doc = word.Documents.Open(path + "/" + file)
                doc.SaveAs(path + "/%sx"%file, 12)  #12代表转换后为docx文件
                doc.Close
                word.Quit()   #结束后台进程
 
 
        # Del doc
        def delDoc(self, path, file):
                time_start=time.time()
                while True:
                        time_end=time.time()
                        wmi = wc.GetObject("winmgmts:")
                        proCodeCov = wmi.ExecQuery('select * from Win32_Process where Name="WINWORD.EXE"')
                        if len(proCodeCov) <= 0:
                                os.remove(path + "/" + file)
                                return
                        time.sleep(3)
                        if time_end - time_start > 20:
                                print('删除 【%s】 文档超时'%file)
                                return
 
 
        # docx path
        def getPath(self):
                root = tk.Tk()
                root.withdraw()
                path = filedialog.askdirectory(title = "选择Word登记表所在目录")
                docs = [i for i in os.listdir(path) if i.endswith(".doc")]
                if docs:
                        print("==================Doc2Docx==================")
                        for doc in docs:
                                self.doc2docx(path, doc)
                                self.delDoc(path, doc)
                                print("%s 已转换为: %s"%(doc, doc+"x"))
                        print("==================Doc2Docx==================\n")
                docxs = [i for i in os.listdir(path) if i.endswith(".docx")]
                return path, docxs
 
 
        # 根据html tr&td 标签分类
        def docxCategory(self, path, docxs):
                docx_cate = {}
 
                for docx in docxs:
                        html = PyDocX.to_html(path + "/%s"%docx)
                        soup = BeautifulSoup(html, 'html.parser')
                        elem = soup.find_all("tr")                              #每个tr标签对应表格的一行                      
                        elem1 = re.sub(r"(?<=<td).+?(?=</td>)", "", str(elem))  #去除单元格标签td之间的内容
 
                        if elem1 in docx_cate.keys():
                                e = docx_cate[elem1]
                                e.append(docx)
                                docx_cate[elem1] = e
                        else:
                                docx_cate[elem1] = [docx]
 
                print("==================docxCategory==================")
                for c, docx in enumerate(docx_cate.values()):
                        path_cate = path + "/_cate/类别%d"%(c+1) 
 
                        if not os.path.exists(path_cate):
                                os.makedirs(path_cate)
 
                        print("类别%d: "%(c+1))
                        for i in docx:
                                print(i, end=" ")
                                # shutil.move("%s/%s"%(path, i), "%s/%s"%(path_cate, i))        #移动
                                shutil.copyfile("%s/%s"%(path, i), "%s/%s"%(path_cate, i))    #复制
                        print()
                print("==================docxCategory==================")
 
 
        # docx2xlsx. 模板命名model.docx,与word放置相同文件夹
        def docx2xlsx(self, path, docxs):
                docxs.remove("model.docx")
 
                # 获取模板文件所需数据的位置
                html = PyDocX.to_html(path + "/model.docx")
                soup = BeautifulSoup(html, 'html.parser')
                elem = soup.find_all("tr")
                data = {}
                for row, tr in enumerate(elem):
                        if tr.text:                           #该行有需要的数据
                                val = {}
                                units = tr.find_all("td")         #获取需要的单元格序号
                                for unit, td in enumerate(units):
                                        if td.text:
                                                val[unit] = td.text
                                data[row] = val
                # 创建xlsx
                xl = wc.Dispatch('Excel.Application')
                xl.Visible = True
                xl.Workbooks.Add()
                xlBook = xl.Workbooks(1)
                xlSheet = xl.Sheets(1)
                # 数据汇总
                try:
                        for c, docx in enumerate(docxs):
                                html = PyDocX.to_html(path + "/%s"%docx)
                                soup = BeautifulSoup(html, 'html.parser')
                                elem = soup.find_all("tr")
                                for r in data.keys():
                                        for u in data[r].keys():
                                                xlSheet.Cells(c+1, int(data[r][u])).Value = elem[r].find_all("td")[int(u)].text.strip()
                except:
                        print(docx,"出错!")
                xlBook.SaveAs(path.replace(r"/", "\\") + "\\result.xlsx")  #实际单\才能正常保存
                # xl.Quit() #关闭
 
 
if __name__ == '__main__':
        d2x = Doc2Xlsx()
        path, docxs = d2x.getPath()
        d2x.docx2xlsx(path, docxs)
        classNeeded = 0
        if classNeeded:
                d2x.docxCategory(path, docxs)