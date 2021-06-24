import sys
import time
import threading
from PyQt5 import QtCore,  QtWidgets
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import  QLCDNumber, QMessageBox
 
 
class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
 
    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        start_time = QDateTime.currentMSecsSinceEpoch()
        #print(start_time)
        #exec('ui.time_refresh(start_time,' + 'ui.lcdNumber_' + self.name + ')')
        function(name=self.name)
        ui.time_refresh(start_time,ui.lcdNumber_BubbleSort)
        #interval = endDate - ui.startDate
        #exec('ui.' + 'lcdNumber_' + self.name + '.display(interval)')
        #exec('ui.time_refresh(start_time,'+'ui.lcdNumber_'+self.name+')')
        ui.finish_counter+=1
        if ui.finish_counter== len(mark):
            ui.Button_start.setText('开始')
            ui.Button_start.setEnabled(True)
            for i in ui.check_boxs:
                i.setEnabled(True)
            ui.Button_random.setEnabled(True)
 
 
def function(name):
    start = time.time()
    copy = data.copy()
    ui.Button_start.setText('正在运行')
    ui.Button_start.setEnabled(False)
    exec(name + '(copy)')
    end = time.time()
    exec('ui.' + 'lcdNumber_' + name + '.display(end - start)')  # +\' 秒\'
 
 
class SelectSort():
    def __init__(self, arr):
        self.start(arr)
 
    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
 
    def start(self, arr):
        length = len(arr)
        for i in range(length):
            the_min = i
            for j in range(i + 1, length):
                if arr[j] < arr[the_min]:
                    the_min = j
            self.swap(arr, the_min, i)
 
class QuickSort():
    def __init__(self, arr):
        self.start(arr, 0, len(arr) - 1)
 
    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
 
    def start(self, array, low, high):
        if low > high:
            return
        pivot = low
        left_p = low
        right_p = high
        while left_p < right_p:
            while array[right_p] >= array[pivot] and left_p < right_p:
                right_p -= 1
            while array[left_p] <= array[pivot] and left_p < right_p:
                left_p += 1
            if left_p < right_p:
                self.swap(array, right_p, left_p)
        self.swap(array, pivot, left_p)
        self.start(array, low, left_p - 1)
        self.start(array, left_p + 1, high)
 
class ShellSort():
    def __init__(self, arr):
        self.start(arr)
 
    def start(self, arr):
        n = len(arr)
        gap = int(n / 2)
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i - gap
                while j >= 0 and arr[j] > temp:
                    arr[j + gap] = arr[j]
                    j = j - gap
                arr[j + gap] = temp
            gap = int(gap / 2)
 
class HeapSort():
    def __init__(self, arr):
        self.start(arr)
 
    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
 
    def Percdown(self, arr, now, length):
        replace = now * 2
        while replace < length:
            right_child = replace + 1
            if right_child < length and arr[replace] < arr[right_child]:
                replace = right_child
            if arr[replace] > arr[now]:
                self.swap(arr, replace, now)
                now = replace
                replace = now * 2
            else:
                break
 
    def start(self, array):
        length = len(array)
        for i in range(length // 2, -1, -1):
            self.Percdown(array, i, length)
        for i in range(length - 1, -1, -1):
            self.swap(array, 0, i)
            self.Percdown(array, 0, i)
 
class RadixSort():
    def __init__(self, arrx):
        self.start(arrx)
 
    def start(self, arr):
        # buckets有十个桶
        buckets = []
        for i in range(10):
            buckets.append([])
        # 基数设置为6位
        for i in range(6):
            for j in arr:
                buckets[(j // int(pow(10, i))) % 10].append(j)
            # 清空 arr
            arr.clear()
            # 重新排序 并放入arr中
            for k in buckets:
                for z in k:
                    arr.append(z)
            # 清空所有桶内容
            for u in buckets:
                u.clear()
 
class MergeSort():
    def __init__(self, arr):
        self.start(arr,0,len(arr)-1)
    def start(self, array,low,high):
        if low<high:
            center=(low+high)//2
            self.start(array,low,center)
            self.start(array,center+1,high)
            self.merge(array,low,center,high)
 
    def merge(self, array, low, center, high):
        num=high-low+1
        point=low
        left_end=center
        right_begin=center+1
        while low<=left_end and right_begin<=high:
            if array[low]<array[right_begin]:
                try:
                    res_arr[point]=array[low]
                except:
                    res_arr.append(array[low])
                point += 1
                low+=1
            else:
                try:
                    res_arr[point]=array[right_begin]
                except:
                    res_arr.append(array[right_begin])
                point += 1
                right_begin+=1
        while low<=left_end:
            try:
                res_arr[point] = array[low]
            except:
                res_arr.append(array[low])
            point += 1
            low+=1
        while right_begin<=high:
            try:
                res_arr[point] = array[right_begin]
            except:
                res_arr.append(array[right_begin])
            point += 1
            right_begin += 1
 
        for i in range(high,high-num,-1):
            array[i]=res_arr[i]
 
class BubbleSort():
    def __init__(self, arr):
        self.start(arr)
 
    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
 
    def start(self, arr):
        length = len(arr)
        for i in range(length):
            for j in range(i + 1, length):
                if arr[j] < arr[i]:
                    self.swap(arr, j, i)
 
 
class Ui_Form(object):
 
    def setupUi(self, Form):
        Form.setObjectName("各种排序算法时间比较")
        Form.resize(914, 552)
        self.finish_counter=0
        self.Button_start = QtWidgets.QPushButton(Form)
        self.Button_start.setGeometry(QtCore.QRect(210, 220, 121, 50))
        self.Button_start.setObjectName("Button_start")
        self.Button_start.setEnabled(True)
        self.Button_start.clicked.connect(lambda :self.Start(Form))
 
        self.Button_random = QtWidgets.QPushButton(Form)
        self.Button_random.setGeometry(QtCore.QRect(90, 20, 141, 40))
        self.Button_random.setObjectName("Button_random")
        self.Button_random.clicked.connect(lambda: self.get_random_nums(Form))
 
        self.Button_port_out = QtWidgets.QPushButton(Form)
        self.Button_port_out.setGeometry(QtCore.QRect(270, 20, 121, 40))
        self.Button_port_out.setObjectName("Save")
        self.Button_port_out.clicked.connect(lambda :self.port_out(Form))
        # ==============
        self.check_Quick = QtWidgets.QCheckBox(Form)
        self.check_Quick.setGeometry(QtCore.QRect(40, 110, 131, 25))
        self.check_Quick.setObjectName("check_Quick")
        self.check_Quick.stateChanged.connect(lambda: self.checkboxState(self.check_Quick))
        self.check_Heap = QtWidgets.QCheckBox(Form)
        self.check_Heap.setGeometry(QtCore.QRect(40, 160, 131, 25))
        self.check_Heap.setObjectName("check_Heap")
        self.check_Heap.stateChanged.connect(lambda: self.checkboxState(self.check_Heap))
        self.check_Shell = QtWidgets.QCheckBox(Form)
        self.check_Shell.setGeometry(QtCore.QRect(40, 210, 131, 25))
        self.check_Shell.setObjectName("check_Shell")
        self.check_Shell.stateChanged.connect(lambda: self.checkboxState(self.check_Shell))
        self.check_Bubble = QtWidgets.QCheckBox(Form)
        self.check_Bubble.setGeometry(QtCore.QRect(40, 260, 131, 25))
        self.check_Bubble.setObjectName("check_Bubble")
        self.check_Bubble.stateChanged.connect(lambda: self.checkboxState(self.check_Bubble))
        self.check_Select = QtWidgets.QCheckBox(Form)
        self.check_Select.setGeometry(QtCore.QRect(40, 310, 131, 25))
        self.check_Select.setObjectName("check_Select")
        self.check_Select.stateChanged.connect(lambda: self.checkboxState(self.check_Select))
        self.check_Radix = QtWidgets.QCheckBox(Form)
        self.check_Radix.setGeometry(QtCore.QRect(40, 360, 131, 25))
        self.check_Radix.setObjectName("check_Radix")
        self.check_Radix.stateChanged.connect(lambda: self.checkboxState(self.check_Radix))
        self.check_Merge = QtWidgets.QCheckBox(Form)
        self.check_Merge.setGeometry(QtCore.QRect(40, 410, 131, 25))
        self.check_Merge.setObjectName("check_Merge")
        self.check_Merge.stateChanged.connect(lambda: self.checkboxState(self.check_Merge))
        #===State_label======
 
        # self.State_label=QtWidgets.QLabel(Form)
        # self.State_label.setGeometry(QtCore.QRect(320, 230,100,30))
        # self.State_label.setText('未运行')
        # self.State_label.setFont(QFont('Arial', 12))
 
        # ====Label_timer====
        self.Label_timer = QtWidgets.QTextEdit(Form)
        self.Label_timer.setGeometry(QtCore.QRect(550, 25, 110, 35))
        self.Label_timer.setText('   时间/秒')
        self.Label_timer.setFont(QFont('Arial',11))
        self.Label_timer.setEnabled(False)
 
 
        self.Label_atttion = QtWidgets.QTextEdit(Form)
        self.Label_atttion.setGeometry(QtCore.QRect(120, 485, 700, 35))
        self.Label_atttion.setText('  同时运算多个算法可以横向比较运行时间，但相比只运行某个算法会花更多时间  ')
        self.Label_atttion.setFont(QFont('Arial',11))
        self.Label_atttion.setEnabled(False)
        #self.Label_timer.
 
        # ====lcdNumber====
        self.lcdNumber_0 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_0.setGeometry(QtCore.QRect(690, 25, 180, 30))
        self.lcdNumber_0.setMode(QLCDNumber.Dec)
        self.lcdNumber_0.setDigitCount(10)
        self.lcdNumber_0.setObjectName("lcdNumber_0")
        self.lcdNumber_0.setStyleSheet("color: black; background: transparent;font:bold;font-family:Arial;")
 
        self.lcdNumber_QuickSort = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_QuickSort.setGeometry(QtCore.QRect(460, 105, 200, 30))
        self.lcdNumber_QuickSort.setMode(QLCDNumber.Dec)
        self.lcdNumber_QuickSort.setDigitCount(8)
        self.lcdNumber_QuickSort.setObjectName("lcdNumber_QuickSort")
 
        self.lcdNumber_HeapSort = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_HeapSort.setGeometry(QtCore.QRect(460, 155, 200, 30))
        self.lcdNumber_HeapSort.setMode(QLCDNumber.Dec)
        self.lcdNumber_HeapSort.setDigitCount(8)
        self.lcdNumber_HeapSort.setObjectName("lcdNumber_HeapSort")
 
        self.lcdNumber_ShellSort = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_ShellSort.setGeometry(QtCore.QRect(460, 205, 200, 30))
        self.lcdNumber_ShellSort.setMode(QLCDNumber.Dec)
        self.lcdNumber_ShellSort.setDigitCount(8)
        self.lcdNumber_ShellSort.setObjectName("lcdNumber_ShellSort")
 
        self.lcdNumber_BubbleSort = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_BubbleSort.setGeometry(QtCore.QRect(460, 255, 200, 30))
        self.lcdNumber_BubbleSort.setMode(QLCDNumber.Dec)
        self.lcdNumber_BubbleSort.setDigitCount(8)
        self.lcdNumber_BubbleSort.setObjectName("lcdNumber_BubbleSort")
 
        self.lcdNumber_SelectSort = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_SelectSort.setGeometry(QtCore.QRect(460, 305, 200, 30))
        self.lcdNumber_SelectSort.setMode(QLCDNumber.Dec)
        self.lcdNumber_SelectSort.setDigitCount(8)
        self.lcdNumber_SelectSort.setObjectName("lcdNumber_SelectSort")
 
        self.lcdNumber_RadixSort = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_RadixSort.setGeometry(QtCore.QRect(460, 355, 200, 30))
        self.lcdNumber_RadixSort.setMode(QLCDNumber.Dec)
        self.lcdNumber_RadixSort.setDigitCount(8)
        self.lcdNumber_RadixSort.setObjectName("lcdNumber_RadixSort")
 
        self.lcdNumber_MergeSort = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_MergeSort.setGeometry(QtCore.QRect(460, 405, 200, 30))
        self.lcdNumber_MergeSort.setMode(QLCDNumber.Dec)
        self.lcdNumber_MergeSort.setDigitCount(8)
        self.lcdNumber_MergeSort.setObjectName("lcdNumber_MergeSort")
 
        # ===timer=====
        self.time_counter = QTimer(Form)
        self.time_counter.setInterval(10)
        self.startDate = QDateTime.currentMSecsSinceEpoch()
        self.time_refresh(self.startDate,self.lcdNumber_0)
        self.time_counter.start()
 
        self.check_boxs=[self.check_Heap,self.check_Bubble,self.check_Radix,self.check_Select,self.check_Quick,self.check_Shell,self.check_Merge]
 
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
 
    def time_refresh(self,start_time,the_lcd):
        self.time_counter.timeout.connect(lambda: self.refresh(start_time,the_lcd))
 
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "各种排序算法时间比较"))
        self.Button_start.setText(_translate("Form", "开始"))
        self.Button_random.setText(_translate("Form", "生成随机数"))
        self.Button_port_out.setText(_translate('Form','保存随机数'))
        self.Button_random.setFont(QFont('Arial',12))
        self.Button_start.setFont(QFont('Arial', 12))
        self.check_Quick.setText(_translate("Form", "QuickSort"))
        self.Button_port_out.setFont(QFont('Arial', 12))
        self.check_Quick.setFont(QFont('Arial',12))
        self.check_Heap.setText(_translate("Form", "HeapSort"))
        self.check_Heap.setFont(QFont('Arial', 12))
        self.check_Shell.setText(_translate("Form", "ShellSort"))
        self.check_Shell.setFont(QFont('Arial', 12))
        self.check_Bubble.setText(_translate("Form", "BubbleSort"))
        self.check_Bubble.setFont(QFont('Arial', 12))
        self.check_Select.setText(_translate("Form", "SelectSort"))
        self.check_Select.setFont(QFont('Arial', 12))
        self.check_Radix.setText(_translate("Form", "RadixSort"))
        self.check_Radix.setFont(QFont('Arial', 12))
        self.check_Merge.setText(_translate("Form", "MergeSort"))
        self.check_Merge.setFont(QFont('Arial', 12))
 
    def refresh(self, startdate,the_lcd):
        #if the_lcd.objectName()!='lcdNumber_0':
        #    print(startdate)
        endDate = QDateTime.currentMSecsSinceEpoch()
        interval = endDate - startdate
        sec = int(int(interval) / 1000)%60
        minute=int(int(int(interval) / 1000)/60)
        hao = int(interval) % 1000
        res = ''
        if minute<=9:
            res+=('0'+str(minute)+':')
        else:
            res+=(str(minute)+':')
        if sec<=9:
            res+=('0'+str(sec)+':')
        else:
            res+=(str(sec)+':')
        if 9 < hao < 100:
            res += ('0' + str(hao))
        elif hao <= 9:
            res += ('00' + str(hao))
        else:
            res += (str(hao))
        #self.lcdNumber_0.display(res)
        the_lcd.display(res)
 
    def checkboxState(self, check_box):
        if check_box.isChecked():
            name = check_box.text()
            if name not in mark:
                mark.append(name)
        else:
            name = check_box.text()
            if name in mark:
                mark.remove(name)
 
    def Start(self,form):
        for i in mark:
            exec('self.lcdNumber_'+i+'.display(0)')
        for i in self.check_boxs:
            i.setEnabled(False)
        self.Button_random.setEnabled(False)
        if len(data) != 0:
            if len(mark)!=0:
                try:
                    self.finish_counter-=self.finish_counter
                    for i in mark:
                        thread1 = myThread(i)
                        thread1.start()
                except:
                    print("Error: unable to start thread")
            else:
                self.mesb = QMessageBox.about(form, '提示', '请至少选择一个算法！！！')
        else:
            self.mesb = QMessageBox.about(form, '提示', '请生成随机数！！！')
 
    def get_random_nums(self, form):
        data.clear()
        the_max = 10000
        import random as ra
        for i in range(the_max):
            data.append(ra.randint(1, 100000))
        self.mesb = QMessageBox.about(form, '提示', '已经生成一万个随机数，范围从0~100000')
 
    def port_out(self,form):
        if len(data)!=0:
            with open(r'data.txt', 'w', encoding='utf-8') as f:
                for i in data:
                    f.write(str(i) + '\n')
            self.mesb = QMessageBox.about(form, '提示', '导出成功')
        else:
            self.mesb = QMessageBox.about(form, '提示', '请生成随机数！！！')
 
 
if __name__ == '__main__':
    mark = []
    data = []
    res_arr=[]
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())