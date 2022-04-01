fresh_fruit = {'apple': 10, 'banana': 8, 'lemon': 5}
if count := fresh_fruit.get('apple', 0):
    print('if block')
else:
    print('else block')

"""
1. 赋值表达式通过海象操作符( := ) 给变量赋值， 并且让这个值成为这条表达式的结果，于是，我们可以利用这项特性来缩减代码
2. 如果赋值表达式是大表达式里的一部分，就得用一对括号把它括起来
3. 虽说 python 不支持 switch/case 与 do/while 结构，但可以利用赋值表达式清晰地模拟出这种逻辑
"""