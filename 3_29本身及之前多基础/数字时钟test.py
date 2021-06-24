from time import time, localtime, sleep # 调用模块也有顺序,time最后报错


# 定义一个数字时钟类
 # 总结下今天写代码的问题：1：self没加。
                       # 2：调用方法show没加()
class Clock_m(object):

    def __init__(self,hour=0 ,minute=0 ,second=0):

        #初始化函数
        self._second = second # self初始函数记得加点.
        self._hour = hour
        self._minute = minute
        # self._second = second
    @classmethod
    def now(cls): # 弄了好久：符号错了，要在英文状态下输入
        ctime = localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec) # 记得加cls就和run加一样
 
    
    def run(self):
        # 定义一个让时间运行的函数
        self._second+= 1
        if self._second == 60: # if语句一般是跟判断，为真则执行以下语句
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1 
                if self._hour == 24:
                    self._hour = 0
    def show(self): # 一般函数最好带个self
        # 定义一个展示时间的函数
        return '%02d:%02d:%02d'%\
            (self._hour,self._minute,self._second)
    
        # @classmethod # 类方法的作用 使用类名直接访问,不加的话就会报TypeError
    # def now(cls): # 类方法内部需调用cls，而不是self
    #     ctime = localtime(time())
    #     return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
# def main():
# disply = Clock_m(11,11,11)
disply = Clock_m.now()
while True:
    print(disply.show()) # show不打括号调用的是执行show方法的对象 <bound method Clock_m.show of <__main__.Clock_m object at 0x000001FC47A13908>>
    sleep(1)
    disply.run()

# if __name__ == '__main__':
#     main()
        