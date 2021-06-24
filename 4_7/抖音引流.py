#python 3.6.4
# encoding:utf-8
 
#确保已连接好adb
#1080 2280 分辨率，一加6测试通过
#抖音版本20200618
 # 吾爱破解上的有空研究下 2021/4/7/19:47
import os
import cv2
import sys
import time
import random
from PIL import Image #pip install pillow  
import diannaoshuohua # 语音提示可关闭
import zhaotu
 
# 上传照片到电脑
def screen():
        # 截图保存在手机上
        os.system('adb shell screencap -p /sdcard/screen.png')
        # 传到电脑上
        os.system('adb pull /sdcard/screen.png')
 
# 截图，粉丝详情页图片
def screen3():
        # 截图保存在手机上
        os.system('adb shell screencap -p /sdcard/screen3.png')
        # 传到电脑上
        os.system('adb pull /sdcard/screen3.png')
 
 
#处理照片
def getDistance():         
        #读取图片
        image = Image.open('screen.png')
        #返回元组
        width = image.size[0]
        height = image.size[1]
        #print(height,width)
 
        for i in range(803,804):#遍历一个纵列
                for j in range(0,height):
                        if image.getpixel((i,j))[:3] == (179, 38, 69):#如果找到符合位置的颜色点，则确定了按钮所在
                                yield j   #生成器。返回所有找到的纵坐标的值
 
def jietu(mubiaotu):
        # 打开刚截取的全屏图
        img = Image.open(mubiaotu)
        # 定位到需要截取的地方
        img = img.crop((0, 200, 1080, 1400))
        # 截取成功并保存到本地
        img.save('screen3_jietu.png')
 
def as_num(x):
    y = '{:.10f}'.format(x)  # .10f 保留10位小数
    return y
 
# 查找图片
def findImg(target1,template2):
        #读取目标图片
        target = cv2.imread(target1)
        #读取模板图片
        template = cv2.imread(template2)
        #获得模板图片的高宽尺寸
        theight,twidth = template.shape[:2]
        #执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
        result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)
        cv2.normalize(result,result, 0, 1, cv2.NORM_MINMAX, -1 )
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        strmin_val = str(min_val)
        cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)
        print ("匹配最小值为："+as_num(float(str(min_val))))
        print ('匹配最大值为：'+as_num(float(str(max_val))))
        r = int((image.getpixel((min_loc[0]+23,min_loc[1]+17)))[0])
        if (abs(float(as_num(float(str(max_val))))) >= 0.9) and r > 180:#如果找到符合位置的颜色点:
                print ('找到符合的图片')
                return True
        else:
                print('没有找到符合的图片')
                return False
 
 
if __name__ == '__main__':#主函数开头
 
        i=0
        n=0
        sj = random.uniform(1,5)
 
         
        for _ in range(100):
                screen()
                print('截屏某用户的粉丝列表')
                xy = zhaotu.findImg2('s.png','screen.png')
                for d in xy:
                        screen()
                        time.sleep(sj)
                        os.system('adb shell input tap {} {}'.format(d[0],d[1]))
                        time.sleep(sj)
                        screen3()#个人详情页截图        
                        time.sleep(sj)
                        jietu('screen3.png')
                        time.sleep(sj)        
                         
                        if zhaotu.findImg1('nv.png','screen3_jietu.png'): 
                                xy = zhaotu.findImg1('nv.png','screen3_jietu.png')
                                image = Image.open("screen3_jietu.png")#打开个人详情页截图
                                r = int((image.getpixel((xy[0],xy[1])))[0])
                                if (r > 180):
                                        print('找到一位女士，即将关注！')
                                        os.system('adb shell input tap 550 466')#点击关注按钮，暂用坐标，待完善
                                        time.sleep(sj)
                                        os.system('adb shell input keyevent 4')
                                        time.sleep(sj)                                         
                                        i=i+1
                                        print('已关注了'+str(i)+'位女士')
                                        if i == 175:
                                                print('本次运行已关注198人，已退出运行！')
                                                diannaoshuohua.shuohua('本次已关注198人，即将退出！')
                                                os.system('adb shell input keyevent 26')#power事件。
                                                sys.exit()
                                else:
                                        os.system('adb shell input keyevent 4') #点击后退按钮        
                        else:
                                print('这不是女士，即将返回！')
                                n=n+1
                                os.system('adb shell input keyevent 4') #点击后退按钮
                                         
                #翻页滑动按钮
                os.system('adb shell input swipe 548 1500 540 225 511')
                time.sleep(random.uniform(0.4, 0.8))
                print('正在翻页。。。')
 
 
#zhaotu.py 调用方法：findImg('目标图片地址','模板图片地址')
#findImg2----多目标匹配，返回的是生成器结果，需要for遍历出单个结果
#findImg1----单目标匹配，返回图片所在位置的中心点坐标值
 
import cv2
import numpy
from PIL import Image
 
def as_num(x):
    y = '{:.10f}'.format(x)  # .10f 保留10位小数
    return y
 
def findImg2(target,template):#opencv模板匹配----多目标匹配
        #读取目标图片
        target = cv2.imread(target)
        #读取模板图片
        template = cv2.imread(template)
        #获得模板图片的高宽尺寸
        theight, twidth = template.shape[:2]
        #执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED  
        print(theight,twidth) 
        result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED) #CV_TM_SQDIFF_NORMED
 
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
 
        cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)
 
        strmin_val = str(min_val)
        #初始化位置参数
        temp_loc = min_loc
        other_loc = min_loc
        numOfloc = 1
        #第一次筛选----规定匹配阈值，将满足阈值的从result中提取出来
        #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法设置匹配阈值为0.01
        threshold = 0.01 #这个值从0.01到0.05之间
        loc = numpy.where(result<threshold)
        if loc:
                #遍历提取出来的位置
                for other_loc in zip(*loc[::-1]):
                    #print(other_loc[0],other_loc[1])
                    yield other_loc
        else:
                return false
 
 
# 查找设定的图片是否包含在另一张图片里
def findImg1(target1,template2):#传入要查找的图片地址和名称，1为大图，2为小图，从大图里查找小图。
        #读取目标图片
        target = cv2.imread(target1)
        theight1,twidth1 = target.shape[:2]
        #读取模板图片
        template = cv2.imread(template2)
        #获得模板图片的高宽尺寸
        theight,twidth = template.shape[:2]
        #执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
        result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)
        #归一化处理
        cv2.normalize(result,result, 0, 1, cv2.NORM_MINMAX, -1 )
        #寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
        #对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
        strmin_val = str(min_val)
        #min_loc：矩形定点
        cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)
        #显示结果,并将匹配值显示在标题栏上
        print ("匹配最小值为："+as_num(float(str(min_val))))
        print ('匹配最大值为：'+as_num(float(str(max_val))))
 
        if (abs(float(as_num(float(str(max_val))))) >= 0.9):# 如果找到
                print ('找到符合的图片')
                return min_loc[0]+twidth1/2,min_loc[1]+theight1/2
        else:
                print('没有找到符合的图片')
                return False