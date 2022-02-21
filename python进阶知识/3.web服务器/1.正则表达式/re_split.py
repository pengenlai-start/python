"""
re 模块 split 方法

根据匹配进行切割字符串，并返回一个列表

"""

import re

ret = re.split(r":| ", "info:xiaozhang 33 shanghai")
print(ret)
