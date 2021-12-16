import socket


def main():
    file_downloader_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_downloader_server.bind(("", 8080))
    file_downloader_server.listen(128)
    new_client_socket, client_addr = file_downloader_server.accept()
    file_name = new_client_socket.recv(1024).decode('utf-8')
    print(f'客户端{client_addr}需要下载的文件是：{file_name}')
    file_content = None
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
        f.close()
    except Exception as e:
        print(f'没有要下载的文件{file_name}')
    if file_content:
        new_client_socket.send(file_content)
    new_client_socket.close()
    file_downloader_server.close()


if __name__ == '__main__':
    main()