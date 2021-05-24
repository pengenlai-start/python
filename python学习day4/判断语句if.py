import random
# inum = int(input("请输入数字："))
# if inum >= 10:
#     print("输入的数字大于10")
# else:
#     print("输入的数字小于10")

irandom = random.randint(1,6)
if irandom < 4:
    print("小", irandom)
else:
    print("大", irandom)

'''
注意：
    代码的缩进为一个 tab 键，或4个空格 —— 建议使用空格
    python 开发中 tab 和空格不要混用！ 否则会报错
    
    if 语句以及 缩进部分是一个完整的代码块
    
    if 和 else 语句以及各自的缩进部分共同是一个完整的代码块
    
逻辑运算符：
    and与    or或     not非   

python 中当条件判断语句过长时，可以对该判断语句加一对括号，再换行
python 能够自动的将一对括号内部的代码连接在一起
eg:
    if(()
        or()
        or()):
    
'''
