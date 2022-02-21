"""
re 模块 search 方法

不是从头开始匹配，但只匹配一个结果，即匹配出一个结果后，就将该结果返回不再管后面的

"""


import re

ret = re.search(r"\d+", "阅读次数1")
print(ret.group())
