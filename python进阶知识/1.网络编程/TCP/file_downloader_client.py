'''
文件下载器，客户端

f = open("xxx")
try:
    f.write()/f.read()
except:
    f.close

with open("xxx") as f:
    f.read()/f.write()

'''

import socket


def main():
    file_downloader_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_ip = input("请输入下载服务器的ip:\n")
    dest_port = input("请输入下载服务器的port:\n")
    file_downloader_client.connect((dest_ip, int(dest_port)))
    download_file_name = input("请输入要下载的文件名字：\n")
    file_downloader_client.send(download_file_name.encode("utf-8"))
    while True:
        recv_data = file_downloader_client.recv(1024)
        if recv_data:
            with open("[新]" + download_file_name, 'ab+') as f:
                f.write(recv_data)
        else:
            break
    file_downloader_client.close()


if __name__ == '__main__':
    main()
