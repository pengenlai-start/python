"""
多态　——　增加代码的灵活度，以继承和重写父类方法为前提

实例　
创建对象：
１）在内存中为对象分配空间
２）调用初始化方法　__init__ 为对象初始化
每个对象都有自己独立的内存空间、保存各自不同的属性
多个对象的方法、在内存中只有一份，在调用方法时，需要把对象的引用传递到方法内部

eg.
class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("1")

class XiaoTian(Dog):
    def game(self):
        print("2")

class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和　%s 快乐玩" % (self.name, dog.name))
        dog.game()

d = Dog("d")
x = XiaoTian("x")
p = Person('p')
p.game_with_dog( d or x)  # 传入参数不同　d or x 调用的对应的　game 方法不一样
"""