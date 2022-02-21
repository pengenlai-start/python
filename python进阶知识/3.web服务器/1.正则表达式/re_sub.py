"""
re 模块 sub 方法

将匹配到的数据进行替换，将所有匹配的字符结果进行替换

"""

import re

ret = re.sub(r"\d+", '将匹配的替换成本字符串', "python=99,c++=123")
print(ret)