"""
gevent 遇见延时操作就执行 —— gevent 里的延时操作

"""
import time
from gevent import monkey
import gevent

# 补丁： 使得 其他的耗时操作能够触发切换
monkey.patch_all()


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)  # 这个延时操作不行
        # gevent.sleep(0.5)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

# g1.join()
# g2.join()
# g3.join()

gevent.joinall([
    gevent.spawn(f, 5),
    gevent.spawn(f, 5),
    gevent.spawn(f, 5)
])

"""
gevent.joinall([
    gevent.spawn(f, 5),
    gevent.spawn(f, 5),
    gevent.spawn(f, 5)
])
和
g1.join()
g2.join()
g3.join()
等价

gevent 是最常用的，协程实现多任务的工具
"""
