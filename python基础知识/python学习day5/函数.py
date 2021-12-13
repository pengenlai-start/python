import random


def cycle_print():
    while True:
        inum = random.randint(0, 100)
        print("inum = %d" % inum)
        if inum == 100:
            break


cycle_print()  # 循环打印随机数的函数

'''
函数
    函数的定义：
        def 函数名():
            函数封装的代码
            ...
            
    函数定义的上方应有两个空行，与上方的代码或者注释
    
    def 函数名():
        """函数说明，函数注释，pycharm ctrl + Q 查看 """
        函数封装的代码
        ...
        return 返回值
        
    return 表示返回，也代表了一个函数的结束，return 后函数的内容不会被执行
'''
