"""
enumerate 自带序号
"""

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i + 1}: {flavor}')

it = enumerate(flavor_list)
print(next(it))
print(next(it))

for i, flavor in enumerate(flavor_list):  # 不指定起始序号
    print(f'{i + 1} : {flavor}')

for i, flavor in enumerate(flavor_list, 1):  # 指定起始序号
    print(f'{i}： {flavor}')

"""
1. enumerate 函数可以用简洁的代码迭代 iterator ，而且可以指出当前这轮循环的序号
2. 不要先通过 range 指定下标的取值范围，然后用下标去访问序列，而是应该直接用 enumerate 函数迭代
3. 可以通过 enumerate 的第二个参数指定起始序号（默认为 0）
"""