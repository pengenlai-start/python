import threading


def test1(temp):
    temp.append(33)
    print(temp)


def main():
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t1.start()


# 多线程间共享全局变量
g_nums = [1, 2]
if __name__ == '__main__':
    main()
