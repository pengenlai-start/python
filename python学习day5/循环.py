import random

while True:
    inum = random.randint(0,100)
    print("inum = %d" % inum)
    if inum == 100:
        break


print("第一个循环结束--------------------------")
idata = 0
while idata <= 100:
    print(idata)
    idata += 1

'''
while 循环的基本语法：
    初始条件设置 —— 通常是重复执行的计数器
    while 条件（判断计数器是否达到目标次数）:
        条件满足时，做的事情
        ...
        处理条件（计数器+1）！！！
'''
