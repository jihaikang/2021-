# 写点批量改文件名的
import os
import re
import sys

#要修改的文件的文件夹路径
path=r"D:\百度网盘企业版\a_pactice\picLibs"
#要批量修改的文件的后缀名为
src_hzm="png"
fileList = os.listdir(path) # 列出该文件夹里的所有文件，这里获取的是一个列表啊
# 输出此文件夹中包含的文件名称
print("修改的文件所在的文件夹路径为：" + path)
# 得到进程当前工作目录
currentpath = os.getcwd() # 获取当前目录
# 将当前工作目录修改为待修改文件夹的位置
os.chdir(path) # 这个改工作目录好厉害啊，工作目录不同会怎样，在python中
# 这个思路不错，不管要执行操作的目录在哪，先获取当前目录os.getcwd(),然后在把当前的目录转化为要操作文档的目录os.chdir(path)
# 接着又改回程序运行前的工作目录
# os.chdir(currentpath)
# 名称变量
num = 1
# 遍历文件夹中所有文件
print(len(fileList))
for fileName in fileList:
        # 匹配文件名正则表达式
        pat = ".+\."+src_hzm
        # 进行匹配
        pattern = re.findall(pat, fileName) # 匹配的正则
        #print(pattern)
        if len(pattern): # 这句话设置长度有什么意思，如果为真就执行，不为真就不执行了。这就是说if有判断真假的作用了，假的就执行else语句了
                print(len(pattern))
                print("正在重命名文件:"+fileName)
                #修改后的后缀名
                det_hzm="jpg"
                #文件重新命名，文件重命名需要的是字符串格式
                os.rename(fileName, ("IMG_"+str(num + 100) + '.' + det_hzm)) # os.rename是专门用来重命名的
                #改变编号，继续下一项
                num = num + 1
        else:
                print("不匹配，跳过文件:"+fileName)
        
print("==========完成===========")
# 改回程序运行前的工作目录
os.chdir(currentpath)
# 刷新
sys.stdin.flush()




