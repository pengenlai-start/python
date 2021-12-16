# TCP 服务器
import socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 7788))
    tcp_server_socket.listen(128)
    # 后面的部分可以添加循环，为多个客户端服务
    while True:
        new_client_socket, client_addr = tcp_server_socket.accept()
        # 后面的部分可添加循环为一个客户端服务多次
        while True:
            recv_data = new_client_socket.recv(1024)  # ctrl + c 强行退出程序， recv 解堵塞有两种方式：1.客户端发送过来数据；
            if not recv_data:                                          # 2.客户端调用close
                break
            else:
                print(recv_data.decode('utf-8'))
            send_data = input()
            new_client_socket.send(send_data.encode('utf-8'))
        new_client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()