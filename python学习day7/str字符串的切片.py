# 字符串的切片——　切片是使用索引值来限定范围，从大字符串中切出小字符串，切片方法适用于字符串，列表，元组
"""
字符串[开始索引:　结束索引:　步长]     [开始索引，结束索引)
０   １   ２   ３   ４   ５       顺序
　 p    y   t    h   o    n
                 -2   -1        逆序

eg.
num_str = '0123456789'
num_str[2: 6]  2345
num_str[2:]    23456789
num_str[0: 6]  012345
num_str[:6]    012345
num_str[:]     0123456789
num_str[::2]   02468
num_str[1::2]  13579
num_str[2:-1]  2345678
num_str[-2:]   89
num_str[0::-1] 0
num_str[::-1] or num_str[-1::-1] 9876543210


非数字型数据的公共方法　——　python内置的函数
len()
del()   del item    del(item)
max()   如果是字典，只针对　key　比较
min()   如果是字典，只针对　key 比较
cmp(item1, item2)   python3　取消了该函数


"""
