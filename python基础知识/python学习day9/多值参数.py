# 多值参数　——　有时候可能需要一个函数能够处理的参数个数是不确定的，这个时候，就可以使用多值参数
"""
在　python 中有两种多值参数：
１）参数名前增加一个　* 可以接收元组
２）参数名前增加两个　* 可以接收字典

１）２）使得调用函数更加简单

一般在给多值参数命名时，习惯使用以下两个名字
１）*args   存放元组参数，前面有一个　*
２）**kwargs    存放字典参数，前面有两个　*

eg

    def demo(num, *args, **kwargs):
        print(num)
        print(args)
        print(kwargs)


    demo(1, 2, 3, 4, 5, name = "小明", age = 18, gender = True)
"""

# 元组和字典的拆包　——　简化元组、字典变量的传递
"""
eg
    def demo(*args, *kwargs):
        print(args)
        print(kwargs)
        
    
    gl_tuple = (1, 2, 3)
    gl_dict = {"name": "小明", "age": 18}
    demo(gl_tuple, gl_dict)  # 两个参数全传给元组!!!!
    拆包：
    demo(*gl_tuple, **gl_dict)
"""