# 先创建 在收发 关闭
# import socket
# # 创建tcp的套接字
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.socket(AddressFamily, Type) 
#Address Family：可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）,实际工作中常用AF_INET
#Type：套接字类型，可以是 SOCK_STREAM（流式套接字，主要用于 TCP 协议）或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）
# 关闭接口
# s.close()

#coding=utf-8
from socket import *

# 1. 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 准备接收方的地址
# '192.168.1.103'表示目的ip地址
# 8080表示目的端口
dest_addr = ('192.168.252.1', 8080)  # 注意 是元组，ip是字符串，端口是数字

# 3. 从键盘获取数据
# send_data = input("请输入要发送的数据:")

# 4. 发送数据到指定的电脑上的指定程序中
# udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
udp_socket.sendto(b"haha",dest_addr)
# 5. 关闭套接字
udp_socket.close() 

