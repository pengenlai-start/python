from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)

print(repr(my_values))

green_str = my_values.get('green', [''])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0

"""
    辅助函数
"""


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    else:
        return default


green = get_first_int(my_values, 'green')

"""
1. python 的语法很容易把复杂的意思挤到同一行表达式里，这样写很难懂
2. 复杂的表达式，尤其是那种需要重复使用的复杂表达式，应该写到辅助函数里面
3. 用 if/else 结构写成的条件表达式，要比用 or 与 and 写成的 Boolean 表达式更好懂
"""
