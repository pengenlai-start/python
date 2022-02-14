"""
协程（gevent） —————— C/C++ 没有

from collections import Iterable

instance(需要判断的数据, Iterable)    判断是否可迭代
"""
import time
from collections.abc import Iterable, Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return ClassIterator(self)


# 迭代器有 __iter__ 和 __next__ 这两个方法，迭代器一定能迭代，但能迭代的不一定会是一个迭代器，迭代有 __iter__ 方法就行
# classmate 和 ClassIterator 可以合并成一个
class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):  # 迭代器需要重写的方法之一，该函数是类是否可迭代的关键，有该函数可迭代，没有该函数不可迭代
        pass

    def __next__(self):  # 迭代器需要重写的方法之一
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration  # 主动抛出异常


if __name__ == '__main__':
    classmate = Classmate()
    classmate.add("老王")
    classmate.add("王五")
    classmate.add("张三")
    """
    for 循环的迭代的实际流程
    
    print("判断classmate 是否是可以迭代的对象：", isinstance(classmate, Iterable))
    classmate_iteator = iter(classmate)
    print("判断 classmate_iterator 是否是迭代器：", isinstance(classmate_iteator, Iterator))
    
    """

    for name in classmate:
        print(name)
        time.sleep(1)
