'''
赋值运算符
    +=      -=      /=      //=     %=      **= ...
'''
import random

inum = random.randint(0,100)
ires = 0
ires += inum
print("ires += %d" % ires)

inum = random.randint(0,100)
ires -= inum
print("ires -= %d" % ires)

inum = random.randint(0,100)
ires /= inum
print("ires /= %d" % ires)

inum = random.randint(0,100)
ires //= inum
print("ires //= %d" % ires)

inum = random.randint(0,100)
ires %= inum
print("ires %%= %d" % ires)

inum = random.randint(0,100)
ires **= inum
print("ires **= %d" % ires)
