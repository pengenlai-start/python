import socket
# 1.创建 套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 2.绑定一个本地信息
local_addr = ("", 8080)  # "" 本地任何一个ip都行
udp_socket.bind(local_addr)  # 必须绑定自己电脑的ip 及 port 其他的不行
# 3.接收数据
recv_data = udp_socket.recvfrom(1024)  # 本次接收数据的最大字节数
# 4.显示接收的数据
print(recv_data)
# 5.关闭
udp_socket.close()

