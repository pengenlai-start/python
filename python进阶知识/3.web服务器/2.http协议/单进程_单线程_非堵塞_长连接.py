import socket
import re

def severce_client(new_socket, request):
    request_lines = request.splitlines()
    print("")
    print(">" * 20)
    print(request_lines)
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"
    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "---------file not found----"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        response_body = html_content
        response_header = "HTTP/1.1 200 OK \r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)  # 长连接，知道本次数据传输完毕的关键
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body
        new_socket.send(response)


def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(("", 7890))
    tcp_server.listen(128)
    tcp_server.setblocking(False)
    client_socket_list = list()
    while True:
        try:
            new_socket, client_addr = tcp_server.accept()
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)
        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as e:
                pass
            else:
                if recv_data:
                    severce_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)
    tcp_server.close()


if __name__ == "__main__":
    main()
