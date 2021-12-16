import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest_addr = ("192.168.31.119", 8080)
send_data = input("请输入要发送的数据：")
udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
udp_socket.close()

