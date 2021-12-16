# TCP 客户端
import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_addr = ("192.168.31.119", 8080)  # 192.168.31.119 是我虚拟机的ip地址
    tcp_socket.connect(tcp_addr)
    while True:
        send_data = input()
        tcp_socket.send(send_data.encode('utf-8'))
        recv_data = tcp_socket.recv(1024)
        if not recv_data:
            break
        print(recv_data.decode('gbk'))
    tcp_socket.close()


if __name__ == '__main__':
    main()
