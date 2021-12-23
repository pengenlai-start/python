import threading
import time


class MyThread(threading.Thread):
    def run(self):  # 继承 Thread 创建多线程的方法中 run 函数必须有
        for i in range(5):
            time.sleep(1)
            msg = f'I\'m {self.name} @ {i}'  # self.name 保存当前线程的名字
            print(msg)


if __name__ == '__main__':
    t = MyThread()
    t.start()  # 会自动调用对应的 run 方法中的程序
