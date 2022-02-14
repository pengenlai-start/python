class Fibonacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration
        

# 除了 for 循环能接收可迭代的对象，list, tuple 等也能接收
li = list(Fibonacci(10))
print(li)

tp = tuple(Fibonacci(10))
print(tp)

fibo = Fibonacci(20)
for num in fibo:
    print(num)
