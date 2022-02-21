"""
re 模块 sub 方法

将匹配到的数据进行替换，将所有匹配的字符结果进行替换,替换的值可以是函数的结果

"""

import re


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


ret = re.sub(r"\d+", add, "python=99,C=10")
print(ret)
# python=100,C=11
