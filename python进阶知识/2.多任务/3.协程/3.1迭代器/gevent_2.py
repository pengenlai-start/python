"""
出结果                                                       出怎么出结果的方法，可迭代的对象
range(10)                                                   xrange(10)
                    python2 中

python3.x 中 range 和 xrange 差不多
"""
# 斐波那契数列
a = 0
b = 1
i = 0
nums = list()

while i < 10:
    nums.append(a)
    a, b = b, a+b
    i += 1

for num in nums:
    print(num)