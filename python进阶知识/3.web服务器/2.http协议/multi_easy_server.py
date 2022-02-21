"""
简单的多进程服务器
"""

import re
import socket
import multiprocessing


def service_socket(new_socket):
    request = new_socket.recv(1024).decode("utf-8")
    request_lines = request.splitlines()
    print("")
    print(">" * 20)
    print(request_lines)
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    print(ret)
    if ret:
        file_name = ret.group(1)
        print(file_name)
        if file_name == "/":
            file_name = "/index.html"
    try:
        f = open("./html"+file_name, "rb")
    except:
        reponse = "HTTP/1.1 404 NOT FOUND\r\n"
        reponse += "\r\n"
        reponse += "-----------file not found --------"
        new_socket.send(reponse.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        reponse = "HTTP/1.1 200 Ok\r\n"
        reponse += "\r\n"
        new_socket.send(reponse.encode("utf-8"))
        new_socket.send(html_content)
    new_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.listen(128)
    while True:
        new_socket, client_addr = tcp_server_socket.accept()
        p = multiprocessing.Process(target=service_socket, args=(new_socket,))
        p.start()
        new_socket.close()  # 多进程需要关闭，因为多进程复制资源，多线程和多进程基本一致，除了不需要在 main 函数中关闭它
    tcp_server_socket.close()


if __name__ == "__main__":
    main()