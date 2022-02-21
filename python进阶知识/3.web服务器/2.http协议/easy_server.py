"""
简单的 http 服务器代码    访问 127.0.0.1：7890

"""

import socket


def service_client(new_socket):
    request = new_socket.recv(1024)
    print(request)
    response = " HTTP/1.1 200 OK\r\n"  # 头
    response += "\r\n"  # 区分头和体
    response += " hahaha"
    new_socket.send(response.encode('utf-8'))
    new_socket.close()


def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 使端口能重复使用
    tcp_server.bind(("", 7890))
    tcp_server.listen(128)
    while True:
        new_socket, client_adder = tcp_server.accept()
        service_client(new_socket)
    tcp_server.close()


if __name__ == "__main__":
    main()


"""
三次握手

syn 请求      ack 应答

client  -------syn 11------------->   server
server  -------ask 12 and syn 44-->   client
client  -------ask 45------------->   server


四次挥手

"""