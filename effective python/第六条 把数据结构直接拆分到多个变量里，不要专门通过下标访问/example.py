"""
这条规则适用于元组的拆分
通过拆分 unpacking 来赋值要比通过下标去访问元组内的元素更清晰，而且这种写法所需的代码量通常比较少
"""
snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
for rank, (name, calories) in enumerate(snacks, 1):
    print(f'#{rank}: {name} has {calories} calories')

"""
1. unpacking 是一种特殊的 python 语法， 只需要一行代码，就能把数据结构里面的多个值分别赋给相应的变量
2. unpacking 在 python 中应用广泛， 凡是可迭代的对象都能拆分，无论它里面还有多少层迭代结构
3. 尽量通过 unpacking 来拆解序列之中的数据， 而不要通过下标访问，这样可以让代码更简洁、更清晰 
"""
