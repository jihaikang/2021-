from socket import *


# 创建套接字
udp_t = socket(AF_INET,SOCK_DGRAM)
# 绑定端口

#进行连接 udp进行连接使用的是sendto
get_ip = input('请输入ip地址：')
get_port = int(input('请输入port：'))
addr = (get_ip,get_port)
# 发送数据
data = input('\n请输入你要输入的数据:')
udp_t.sendto(data.encode('gbk'),addr) #  之力我把encode写成了encound

# 关闭接口
udp_t.close()