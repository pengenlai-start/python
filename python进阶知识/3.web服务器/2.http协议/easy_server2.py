"""
简单的 http 服务器代码

"""

import socket
import re


def service_client(new_socket):
    request = new_socket.recv(1024).decode("utf-8")
    request_lines = request.splitlines()
    print("")
    print(">" * 50)
    print(request_lines)
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        print(ret.group())
        if file_name == "/":
            file_name = "/index.html"
    try:
        f = open("./html" + file_name, "rb")
    except Exception as e:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
    else:
        html_content = f.read()
        f.close()
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        new_socket.send(response.encode("utf-8"))
        new_socket.send(html_content)
    new_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.listen(128)
    while True:
        new_socket, client_addr = tcp_server_socket.accept()
        service_client(new_socket)
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
