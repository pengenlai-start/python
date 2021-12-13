import random


def cycle_print():
    print("这是一个模块")
    while True:
        inum = random.randint(0, 100)
        print("inum = %d" % inum)
        if inum == 100:
            break
