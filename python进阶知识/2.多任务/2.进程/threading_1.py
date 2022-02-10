"""
进程
子进程拥有全进程的资源   代码共享，写时拷贝
"""
import threading
import time
import multiprocessing


def test1():
    while True:
        print("1")
        time.sleep(1)


def test2():
    while True:
        print("2")
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()

'''
线程不能独立执行，必须依存在进程中

线程执行开销小，但不利于资源的管理和保护；而进程正相反
'''