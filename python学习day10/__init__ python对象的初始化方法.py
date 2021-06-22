"""
python 对象的初始化方法　__init__    专门用来定义一个类具有哪些属性的方法  创建对象时，被自动调用
eg.
    class Cat(object):
        def __init__(self, name=""):
            self.name = name

在　__init__　内部定义属性：  self.属性名　= 属性的初始值

定义没有初始值的属性
１）　None 关键字表示什么都没有      要用　is 判断
２）　表示一个空对象，没有方法和属性，是一个特别的常量
３）　可以将　None 赋值给任何一个变量

"""