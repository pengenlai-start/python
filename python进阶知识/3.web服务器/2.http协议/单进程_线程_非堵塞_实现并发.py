import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(("", 7890))
tcp_server.listen(128)
tcp_server.setblocking(False)  # 设置套接字为非堵塞方式
client_socket_list = list()

while True:
    try:
        new_socket, client_addr = tcp_server.accept()
    except Exception as ret:
        print("没有新客户端")
    else:
        print("来了新客户端")
        new_socket.setblocking(False)
        client_socket_list.append(new_socket)
    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024)
        except Exception as ret:
            print("没有数据")
        else:
            if recv_data:
                print("来了数据")
            else:
                client_socket_list.remove(client_socket)
                client_socket.close()

tcp_server.close()


"""
1.1 
长连接 ---> 建立连接 --- 数据传输 --- (保持连接) --- 数据传输 --- 关闭连接

1.0
短连接 ---> 建立连接 --- 数据传输 --- 关闭连接 --- 建立连接 --- 数据传输 --- 关闭连接


"""

