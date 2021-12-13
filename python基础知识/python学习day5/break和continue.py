import random

i = 0
while i <= 100:
    if i == 44:
        i += 1
        continue  # 跳过本次循环，不执行其后的循环语句
    print("i = %d" % i)
    i += 1

print("=" * 20)
i = 0
while i <= 100:
    if i == 44:
        i += 1
        break  # 跳出循环，结束循环
    print("i = %d" % i)
    i += 1

