import random

while True:
    inum = random.randint(0,100)
    if inum == 100:
        break
    elif inum == 44:
        continue  # 44不会打印出来
    print(inum, end="| ")  # end='符号'   以什么符号作为结束，默认是换行
