from socket import *


# 创建套接字 
tcp_t = socket(AF_INET,SOCK_STREAM)  # 这里把socket写成了scoket tcp_t = scoket.scoket(AF_INET,SOCK_STREAM)
# 连接服务器
addip = input('请输入ip地址：')
addop = int(input('请输入端口号：'))
tcp_t.connect((addip,addop))
# 发送数据send
data = input('请输入传输的文字：')
tcp_t.send(data.encode('gbk')) # 这里写成了endoce 服了encode decode

# 指定数据长短 
recv_data = tcp_t.recv(1024) #  这里不需要加引号
print('输入的数据是%：', recv_data.decode('gbk'))
# 断开连接
tcp_t.close()