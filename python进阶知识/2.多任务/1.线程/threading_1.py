import time
import threading


def sing():
    for i in range(5):
        print("唱歌")
        time.sleep(1)


def dance():
    for i in range(5):
        print("跳舞")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    # 多线程执行到这儿的时候，主程序依次执行，t1.start()、t2.start()
    # 主程序执行到 t1.start() 的时候会开出一个分支去单独执行 t1.start() 中的程序
    # 主程序执行到 t2.start() 的时候又会开出一个分支去单独执行 t2.start() 中的程序
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()