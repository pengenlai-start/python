"""
进程池 pool
"""


import os
import random
import time
from multiprocessing import Pool


def worker(msg):
    t_start = time.time()
    print(f'{msg} 开始执行，进程号为 {os.getpid()}')
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(f'{msg} 执行完毕，耗时{t_stop - t_start:.2f}')


if __name__ == '__main__':
    po = Pool(3)  # Pool 在使用的时候必须放到 if __name__ == '__main__': 下否则会报错
    for i in range(0, 10):
        po.apply_async(worker, (i,))
    print("----start----")
    po.close()
    po.join()  # 等待 po 中所有的进程执行完成，必须放在 close 之后
    print("----end----")
