"""
gevent 遇见延时操作就执行 —— gevent 里的延时操作

"""
import time

import gevent


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)  # 这个延时操作不行
        gevent.sleep(0.5)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

g1.join()
g2.join()
g3.join()
