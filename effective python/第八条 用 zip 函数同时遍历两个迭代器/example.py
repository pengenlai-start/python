names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
longest_name = None
max_count = 0

for name, count in zip(names, counts):  # 只要其中任何一个迭代器处理完毕，就不再向下走了。以最短的为准
    if count > max_count:
        max_count = count
        longest_name = name

print(f'{longest_name}: {max_count}')

import itertools

names.append('pel')
for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')

"""
1. 内置的 zip 函数可以同时遍历多个迭代器
2. zip 会创建惰性生成器，让它每次只生成一个元组，所以无论输入的数据有多长，它都是一个一个处理的
3. 如果提供的迭代器的长度不一致，那么只要其中任何一个迭代完毕，zip 就会停止
4. 如果想按最长的那个迭代器来遍历，那就改用内置的 itertools 模块中的 zip_longest 函数
"""

