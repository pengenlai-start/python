for i in range(3):
    print(f'{i}')
else:
    print('Else block')


while False:
    print('Never runs')
else:
    print('while Else block')


"""
1. python 有种特殊的语法，可以把 else 块紧跟在整个 for 循环或 while 循环的后面。
2. 只有在整个循环没有因为 break 提前跳出的情况下， else 块才会执行
3. 把 else 块紧跟在整个循环后面，会让人不太容易看出这段代码的意思，所以要避免这样写
"""