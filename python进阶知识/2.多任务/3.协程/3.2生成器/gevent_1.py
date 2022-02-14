"""
生成器 —— 特殊的迭代器

1.创建生成器的方法
nums = [x*2 for x in range(10)]  # 占空间， x*2 for x in range(10) 为 列表生成式
[0, 2, 4, 6, 8, 10, ..., 18]

nums = (x*2 for x in range(10))  # 生成器，返回数据生成方式，节省空间
for num in nums:
    print(num)          0   2   4   6   ... 18

2.创建生成器的第二种方法 —— 函数中有 yield, 通过 yield 让其执行

def create_num(num):
    a, b = 0, 1
    current_num = 0
    while current_num < num:
        # print(a)
        # ret = yield a
        yield a  # 如果一个函数中有 yield 语句，那么这个就不是函数，而是一个生成器模板
        a, b = b, a+b
        current_num += 1
"""

def create_num(num):
    a, b = 0, 1
    current_num = 0
    while current_num < num:
        print("a = ", a)
        ret = yield a
        print("ret = ", ret)
        # yield a  # 如果一个函数中有 yield 语句，那么这个就不是函数，而是一个生成器模板
        a, b = b, a+b
        current_num += 1


# obj = create_num(10)
# for num in obj:
#     print(num)

obj = create_num(10)
ret = next(obj)  # 通过 next 来启动生成器
print("ret", ret)
ret = obj.send("haha")  # 通过 send 来启动生成器, 不能通过 send 来启动第一次，除非传 None

"""

这个表达式分为左右两部分，yield a，这个意思就是生成器中a的值传出去，然后将这个对象赋值给 next（）或者for这种函数，对吧。我们要主要的是，yield a的时候，生成器就已经出现了阻塞，类似于阻塞吧，生成器是有上下文的，他会记录yield 之后的状态，并且下一次调用的时候，会自动继续迭代，保留了之前的结果。
yield a的时候，我们知道第一个ret的值就是第一次满足while循环条件的 a的值，就是 0。
那我们还知道一种启动生成器的方法有两种，一个是next（）方法，或者说是包含next魔法函数这种对对象，第二个是协程中非常重要的概念，就是生成器对象的send（），当然，需要在生成器中有一个对象来接受yeild a的值，我们把他也设定ret。
非常重要的一点就是函数只进行了右侧的生成器取值过程，而没有进行赋值给ret的操作。
所以，下次利用send（）方法再次启动生成器的时候，会先赋值给ret，然后进行 a，b对象的指针内存的改变（a，b交换值,并且b += a），然后符合while的条件，继续进入loop，到达yield a，然后把此时的a的值，赋值给ret，然后线程又到了阻塞的时候，等待着唤醒（send（）或者next魔法函数的对象）
当 return的时候，就没有yield存在了，再次运行next魔法函数就会报错了。StopIteration异常。

"""
