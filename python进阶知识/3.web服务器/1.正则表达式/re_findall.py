"""
re 模块 findall 方法

找出所有符合匹配表达式的数据

"""

import re


ret = re.findall(r"\d+", "python=99,c=56,c++=45")
print(ret)
