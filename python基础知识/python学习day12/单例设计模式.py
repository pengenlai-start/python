"""
单例设计模式
    __new__ 方法　　是一个由 object 基类提供的内置静态方法，在内存中为对象分配空间，返回对象的引用

    python 解释其获得对象的引用后将引用作为第一个参数（self），传递给　__init__ 方法

    重写　__new__ 方法的代码十分固定，静态方法，在调用时需要主动传递　cls 参数
    １）重写　__new__ 方法一定要　return super().__new__(cls)
    2) 否则　Python 的解释器得不到分配了空间的对象引用，就不会调用对象的初始化方法

单例代码
    class Singleton(object):
        instance = None
        def __new__(cls,*args,**kwargs):
            if cls.instance is None:
                cls.instance = super().__new__(cls)
            return cls.instance

"""