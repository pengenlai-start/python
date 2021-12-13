import random  # 导入随机数需要的包

while True:
    inum = random.randint(0,100)  # [0,100]
    if inum == 66:
        print("luckey",inum)
    elif inum == 99:
        print("good job",inum)
    elif inum == 100:
        break
    else:
        print(inum)
