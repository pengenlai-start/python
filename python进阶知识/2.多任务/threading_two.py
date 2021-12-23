"""
如果创建 Thread 时执行的函数运行结束，那么意味着这个子线程结束了
主线程会等待子线程先结束

当调用 Thread 的时候，不会创建线程
当调用 Thread 创建出来的实例对象的 start 方法的时候才会创建线程以及让这个线程开始运行
"""
import threading
import time


def test1():
    for i in range(5):
        print(i)
        time.sleep(1)


def test2():
    for i in range(10):
        print(i)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())  # threading.enumerate() 查看线程数信息
        if len(threading.enumerate()) == 1:
            break
        time.sleep(1)


if __name__ == '__main__':
    main()

